from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

from django.dispatch import Signal

User = get_user_model()
UserModel = get_user_model()

user_logged_in = Signal()

from django.dispatch import Signal

# signal sent when users successfully recover their passwords
user_recovers_password = Signal(
)


def customer_profile(sender, instance, created, **kwargs):
    if created:
        print('Profile created!')


post_save.connect(customer_profile, sender=User)
