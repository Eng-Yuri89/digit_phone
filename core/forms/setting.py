from django import forms
from django.contrib.sites.models import Site

from core.models.design import Setting, Country, SeoSetting, ExtraSetting, SettingFeatures, SettingSkills


class AdminSettingForm(forms.ModelForm):
    class Meta:
        model = Setting
        fields = '__all__'


class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = '__all__'



class AdminCountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = '__all__'
        exclude = ['setting']


class AdminExtraSettingForm(forms.ModelForm):
    class Meta:
        model = ExtraSetting
        fields = '__all__'
        exclude = ['setting']


class AdminSeoSettingForm(forms.ModelForm):
    class Meta:
        model = SeoSetting
        fields = '__all__'
        exclude = ['setting']


class AdminSettingFeaturesForm(forms.ModelForm):
    class Meta:
        model = SettingFeatures
        fields = '__all__'
        exclude = ['setting']


class AdminSettingSkillsForm(forms.ModelForm):
    class Meta:
        model = SettingSkills
        fields = '__all__'
        exclude = ['setting']
