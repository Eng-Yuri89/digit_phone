from django.conf import settings
# for HTML Email
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from core.models.design import Setting
from core.models.notifications import Notification

############ Enmail  Notifcation ##################

def notify_admin(data):
    from_email = settings.DEFAULT_EMAIL_FROM
    site_setting = Setting.objects.all()

    for setting in site_setting:
        to_email = setting.email
        subject = 'New Vendor Accepted'
        text_content = 'You have a New Vendor Accepted!'
        html_content = render_to_string('email_notification/email_notify_admin.html', {'data': data, 'vendor': setting})

        msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
        msg.attach_alternative(html_content, 'text/html')
        msg.send()


############ Dashboard Notifcation ##################

def create_notification_admin(request, to_user, notification_type, extra_id=0 ,extra_info=0):

    for user in to_user:
     notification = Notification.objects.create(to_user=user, notification_type=notification_type , extra_id=extra_id,
                                               extra_info=extra_info)

