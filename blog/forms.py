import logging

from django import forms
from django.forms import ModelForm
# from haystack.forms import SearchForm
from tinymce.widgets import TinyMCE

from blog.models import Article, Tag, Category

logger = logging.getLogger(__name__)


class AdminArticleForm(ModelForm):
    body = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    slug = forms.SlugField(required=False)

    class Meta:
        model = Article
        fields = '__all__'
        exclude = ['pub_time', 'views']


class AdminArticleCategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class AdminArticleTagTagForm(ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'

#
# class BlogSearchForm(SearchForm):
#     querydata = forms.CharField(required=True)
#
#     def search(self):
#         datas = super(BlogSearchForm, self).search()
#         if not self.is_valid():
#             return self.no_query_found()
#
#         if self.cleaned_data['querydata']:
#             logger.info(self.cleaned_data['querydata'])
#         return datas
