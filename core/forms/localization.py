from django.forms import ModelForm

from core.models.localization import Country, Governorates, City, Language, Currency, Area


class AdminLanguageForm(ModelForm):
    class Meta:
        model = Language
        fields = '__all__'


class AdminCurrencyForm(ModelForm):
    class Meta:
        model = Currency
        fields = '__all__'
        exclude = ['exchange']


class AdminCountryForm(ModelForm):
    class Meta:
        model = Country
        exclude = ['slug']


class AdminGovernoratesForm(ModelForm):
    class Meta:
        model = Governorates
        exclude = ['slug']


class AdminCityForm(ModelForm):
    class Meta:
        model = City
        exclude = ['slug']


class AdminAreaForm(ModelForm):
    class Meta:
        model = Area
        exclude = ['slug']
