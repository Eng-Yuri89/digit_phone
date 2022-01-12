from django.forms import ModelForm

from lawyer.models import Court, CourtCircuit


class AdminCourtForm(ModelForm):

    class Meta:
        model = Court
        fields = '__all__'
        exclude=['court_code']


class AdminCourtCircuitForm(ModelForm):

    class Meta:
        model = CourtCircuit
        fields = '__all__'
        exclude=['circuit_code']

