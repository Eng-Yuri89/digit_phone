from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.contrib.auth import (
    login as auth_login,
)
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth.models import Group
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ValidationError
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.shortcuts import resolve_url
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.translation import gettext_lazy as _
from django.views import View
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import FormView, TemplateView

from core.decorators import unauthenticated_user
from core.forms.users import PasswordResetForm, SetPasswordForm, UserLoginForm
from user.forms.forms import UserSignUpForm
from user.signals import user_logged_in

User = get_user_model()
UserModel = get_user_model()


@unauthenticated_user
def UserSignup(request):
    if request.method == 'GET':
        return render(request, 'users/dashboard/CustomerRegister.html')
    if request.method == 'POST':
        groups = Group.objects.get_or_create(name='customer')
        form = UserSignUpForm(request.POST)
        # print(form.errors.as_data())
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            group = Group.objects.get(name='customer')
            group.user_set.add(user)
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('users/dashboard/UserActiveEmailMessage.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return render(request, 'users/dashboard/UserActiveEmailSent.html')
    else:
        form = UserSignUpForm()
    return render(request, 'users/dashboard/CustomerRegister.html', {'form': form})


@unauthenticated_user
def UserActivate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, 'users/dashboard/UserActiveEmailDone.html')
    else:
        return render(request, 'users/dashboard/UserActiveEmailInvalid.html')


# @unauthenticated_user
class UserLogin(View):
    """
    Description:Will be used to login and logout users.\n
    """
    template_name = 'users/dashboard/CustomerLogin.html'

    def get(self, request, *args, **kwargs):
        form = UserLoginForm()
        context = {
            "title": "Login",
            "form": form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = UserLoginForm(request.POST or None)

        next_ = request.GET.get('next')
        next_post = request.POST.get('next')
        redirect_path = next_ or next_post or None

        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            remember_me = form.cleaned_data['remember_me']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                if not remember_me:
                    request.session.set_expiry(
                        0)  # <-- Here if the remember me is False, that is why expiry is set to 0 seconds. So it will automatically close the session after the browser is closed.

            if user is not None:
                login(request, user)
                user_logged_in.send(
                    user.__class__,
                    instance=user,
                    request=request
                )

                return redirect("/")

            else:
                print("error")
                return redirect("/login/")

        context = {
            "title": "Login",
            "form": form
        }
        return render(request, self.template_name, context)


def UserLogout(request):
    logout(request)
    return redirect('home:HomeIndex')


################Profile##############


###########Rest Password#############
INTERNAL_RESET_SESSION_TOKEN = '_password_reset_token'


class PasswordContextMixin:
    extra_context = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': self.title,
            **(self.extra_context or {})
        })
        return context


class PasswordResetView(PasswordContextMixin, FormView):
    email_template_name = 'users/RestPassword/password_reset_email.html'
    extra_email_context = None
    form_class = PasswordResetForm
    from_email = None
    html_email_template_name = None
    subject_template_name = 'users/RestPassword/password_reset_subject.txt'
    success_url = reverse_lazy('user:passwordResetDone')
    template_name = 'users/RestPassword/password_reset_form.html'
    title = _('Password reset')
    token_generator = default_token_generator

    @method_decorator(csrf_protect)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        opts = {

            'use_https': self.request.is_secure(),
            'token_generator': self.token_generator,
            'from_email': self.from_email,
            'email_template_name': self.email_template_name,
            'subject_template_name': self.subject_template_name,
            'request': self.request,
            'html_email_template_name': self.html_email_template_name,
            'extra_email_context': self.extra_email_context,
        }
        form.save(**opts)
        return super().form_valid(form)


class PasswordResetDoneView(PasswordContextMixin, TemplateView):
    template_name = 'users/RestPassword/password_reset_done.html'
    title = _('Password reset sent')


class PasswordResetConfirmView(PasswordContextMixin, FormView):
    form_class = SetPasswordForm
    post_reset_login = False
    post_reset_login_backend = None
    reset_url_token = 'set-password'
    success_url = reverse_lazy('user:passwordResetComplete')
    template_name = 'users/RestPassword/password_reset_confirm.html'
    title = _('Enter new password')
    token_generator = default_token_generator

    @method_decorator(sensitive_post_parameters())
    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        assert 'uidb64' in kwargs and 'token' in kwargs

        self.validlink = False
        self.user = self.get_user(kwargs['uidb64'])

        if self.user is not None:
            token = kwargs['token']
            if token == self.reset_url_token:
                session_token = self.request.session.get(INTERNAL_RESET_SESSION_TOKEN)
                if self.token_generator.check_token(self.user, session_token):
                    # If the token is valid, display the password reset form.
                    self.validlink = True
                    return super().dispatch(*args, **kwargs)
            else:
                if self.token_generator.check_token(self.user, token):
                    # Vendor the token in the session and redirect to the
                    # password reset form at a URL without the token. That
                    # avoids the possibility of leaking the token in the
                    # HTTP Referer header.
                    self.request.session[INTERNAL_RESET_SESSION_TOKEN] = token
                    redirect_url = self.request.path.replace(token, self.reset_url_token)
                    return HttpResponseRedirect(redirect_url)

        # Display the "Password reset unsuccessful" page.
        return self.render_to_response(self.get_context_data())

    def get_user(self, uidb64):
        try:
            # urlsafe_base64_decode() decodes to bytestring
            uid = urlsafe_base64_decode(uidb64).decode()
            user = UserModel._default_manager.get(pk=uid)
        except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist, ValidationError):
            user = None
        return user

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.user
        return kwargs

    def form_valid(self, form):
        user = form.save()
        del self.request.session[INTERNAL_RESET_SESSION_TOKEN]
        if self.post_reset_login:
            auth_login(self.request, user, self.post_reset_login_backend)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.validlink:
            context['validlink'] = True
        else:
            context.update({
                'form': None,
                'title': _('Password reset unsuccessful'),
                'validlink': False,
            })
        return context


class PasswordResetCompleteView(PasswordContextMixin, TemplateView):
    template_name = 'users/RestPassword/password_reset_complete.html'
    title = _('Password reset complete')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['login_url'] = resolve_url(settings.LOGIN_URL)
        return context


@login_required
def password(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordForm(request.user)
    return render(request, 'core/password.html', {'form': form})


def TestPages(request):
    return render(request, 'TestPage.html')
