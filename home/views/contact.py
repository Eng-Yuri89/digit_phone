from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage, BadHeaderError, send_mail, EmailMultiAlternatives
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.conf import  settings
from django.template import RequestContext
from django.template.loader import render_to_string

from core.forms.contact import ContactForm
from core.models.services import Contact
from core.utils.utilities import  notify_admin, create_notification_admin
from user.models import User


def contact_view(request):
    user=User.objects.all()
    if request.method == 'POST':
        data = Contact()
        form = ContactForm(request.POST)
        if form.is_valid():
            data.save()
            # Send Email & Notification
            try:

                create_notification_admin(request ,user, 'NewOrder', extra_id=data.id,
                                           extra_info=data.message)

                notify_admin(data)
            except Exception as e:
                print(e)


    form = ContactForm()
    context = {'form': form}
    return render(request, 'front/message-sent.html', context)


#
# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             subject = "Website Inquiry"
#             body = {
#                 'name': form.cleaned_data['name'],
#                 'email': form.cleaned_data['email'],
#                 'message': form.cleaned_data['message'],
#             }
#             message = "\n".join(body.values())
#             send_mail(subject,message,settings.EMAIL_HOST_USER,['info@digithup.com'],fail_silently=False)
#
#             try:
#                 email = EmailMessage(subject, message, from_email=form.cleaned_data['email'], to=['digithup@hmail.com'],
#                                      headers={'Content-Type': 'text/plain'},
#                                      )
#                 email.send()
#             except BadHeaderError:
#                 return HttpResponse('Invalid header found.')
#             return redirect("home:HomeIndex")
#
#     form = ContactForm()
#     return render(request, "front/message-sent.html", {'form': form})


