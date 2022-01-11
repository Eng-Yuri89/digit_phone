from django import forms
from django.forms import ModelForm
from tinymce.widgets import TinyMCE

from core.models.services import Categories, Tags, Services, OurWork, Products, ProductSkills, Features


class AdminCategoryForm(ModelForm):
    class Meta:
        model = Categories
        fields = '__all__'


class AdminTagsForm(ModelForm):
    class Meta:
        model = Tags
        fields = '__all__'


class AdminServicesForm(ModelForm):
    long_desc = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Services
        fields = '__all__'


class AdminWorkForm(ModelForm):
    long_desc = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = OurWork
        fields = '__all__'


class AdminProductForm(ModelForm):
    long_desc = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Products
        fields = '__all__'


class AdminFeaturesForm(ModelForm):
    class Meta:
        model = Features
        fields = '__all__'
        exclude = ['product']


class AdminProductSkillsForm(ModelForm):
    class Meta:
        model = ProductSkills
        fields = '__all__'
        exclude = ['product']
