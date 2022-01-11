from django import forms

from core.models.design import Banners, Slider


class SliderAddForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = '__all__'


class BannersAddForm(forms.ModelForm):
    class Meta:
        model = Banners
        fields = '__all__'
        widgets = {
            'position': forms.Select(attrs={'class': 'custom-select'}),

        }
