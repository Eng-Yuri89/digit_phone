from django import forms


# Create your forms here.
from django.forms import ModelForm

from core.models.services import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

