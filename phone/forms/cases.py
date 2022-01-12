from django.forms import ModelForm, forms

from lawyer.models.cases import CasesType, Cases, ClientTypeCases, CasesUpdate


class AdminCasesTypeForm(ModelForm):


    class Meta:
        model = CasesType
        fields = '__all__'
        exclude=['type_code','slug','code']


class AdminCivilCasesTypeForm(ModelForm):

    class Meta:
        model = Cases
        fields = '__all__'
        exclude=['type_code','slug','code']

class AdminClientCasesTypeForm(ModelForm):

    class Meta:
        model = ClientTypeCases
        fields = '__all__'


class AdminCasesUpdateTypeForm(ModelForm):

    class Meta:
        model = CasesUpdate
        fields = '__all__'
