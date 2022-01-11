from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import UpdateView, CreateView, ListView, DetailView, DeleteView

from core.decorators import superuser_only, unauthenticated_user, authenticated_user
from user.forms.forms import UserLoginForm
from user.signals import user_logged_in

User = get_user_model()


class AdminLogin(View):
    """
    Description:Will be used to login and logout users.\n
    """
    template_name = 'backend/login.html'

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

                return redirect("/dashboard/")

            else:
                print("error")
                return redirect("/dashboard/login/")

        context = {
            "title": "Login",
            "form": form
        }
        return render(request, self.template_name, context)

    @method_decorator(unauthenticated_user)
    def dispatch(self, *args, **kwargs):
        return super(AdminLogin, self).dispatch(*args, **kwargs)


class AdminLockscreen(View):
    """
    Description:Will be used to login and logout users.\n
    """
    template_name = 'users/lockscreen.html'

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
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)

            if user is not None:
                login(request, user)
                user_logged_in.send(
                    user.__class__,
                    instance=user,
                    request=request
                )
                return redirect("/dashboard/")

            else:
                print("error")
                return redirect("/dashboard/login/")

        context = {
            "title": "Login",
            "form": form
        }
        return render(request, self.template_name, context)

    @method_decorator(authenticated_user)
    def dispatch(self, *args, **kwargs):
        return super(AdminLockscreen, self).dispatch(*args, **kwargs)


@login_required(login_url='/login')
def AdminLogout(request):
    logout(request)
    messages.success(request, "Logout Successfully!")
    return HttpResponseRedirect(reverse_lazy("core:AdminLogin"))


class AdminUsersList(ListView):
    model = User
    template_name = 'users/admin.html'
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(AdminUsersList, self).dispatch(*args, **kwargs)


class AdminUserDetail(DetailView):
    model = User
    template_name = 'users/details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(AdminUserDetail, self).dispatch(*args, **kwargs)


class AdminUserCreate(CreateView):
    model = User
    fields = '__all__'
    # form_class = AdminCategoryForm
    template_name = 'users/add.html'
    success_url = reverse_lazy('core:AdminUser')

    # @method_decorator(superuser_only)
    # def dispatch(self, *args, **kwargs):
    #     return super(CategoriesCreate, self).dispatch(*args, **kwargs)


class CategoriesUpdate(UpdateView):
    model = User
    # form_class = AdminCategoryForm
    template_name = 'catalog/category/update.html'
    success_url = reverse_lazy('core:AdminCategory')

    # @method_decorator(superuser_only)
    # def dispatch(self, *args, **kwargs):
    #     return super(CategoriesUpdate, self).dispatch(*args, **kwargs)


class AdminUserDelete(DeleteView):
    model = User
    fields = '__all__'
    success_url = reverse_lazy('core:AdminUsers')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(AdminUserDelete, self).dispatch(*args, **kwargs)


class AdminUserGroupList(ListView):
    model = Group
    template_name = 'users/UserGroup/admin-group-list.html'

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(AdminUserGroupList, self).dispatch(*args, **kwargs)


class AdminUserGroupCreate(CreateView):
    model = Group
    fields = '__all__'
    template_name = 'users/UserGroup/admin-group-create.html'
    success_url = reverse_lazy('core:AdminUserGroupList')

    # @method_decorator(superuser_only)
    # def dispatch(self, *args, **kwargs):
    #     return super(AdminUserGroupCreate, self).dispatch(*args, **kwargs)


class AdminUserGroupEdit(UpdateView):
    model = Group
    fields = '__all__'
    template_name = 'users/UserGroup/admin-group-update.html'
    success_url = reverse_lazy('core:AdminUserGroupList')

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(AdminUserGroupEdit, self).dispatch(*args, **kwargs)


class AdminUserGroupDelete(DeleteView):
    model = Group
    fields = '__all__'
    success_url = reverse_lazy('core:AdminUserGroupList')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(AdminUserGroupDelete, self).dispatch(*args, **kwargs)
