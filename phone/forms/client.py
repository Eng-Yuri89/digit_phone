from django.forms import ModelForm

from phone.models import IMEI, Client


class AdminClientForm(ModelForm):

    class Meta:
        model = Client
        fields = '__all__'
        exclude=['client_code']


class AdminIMEIForm(ModelForm):
    class Meta:
        model = IMEI
        fields = '__all__'
        exclude= ['client','imei_code']


