import logging

from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from blog.forms import AdminArticleForm, AdminArticleTagTagForm, AdminArticleCategoryForm
from blog.models import Article, Category, Tag
from core.decorators import superuser_only

# Create your views here.

logger = logging.getLogger(__name__)


class AdminArticleList(ListView):
    model = Article
    template_name = 'blog/admin.html'

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(AdminArticleList, self).dispatch(*args, **kwargs)


class ArticleDetail(DetailView):
    model = Article
    context_object_name = 'category'
    template_name = 'blog/details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(ArticleDetail, self).dispatch(*args, **kwargs)


class ArticleCreate(CreateView):
    model = Article
    # fields = '__all__'
    form_class = AdminArticleForm
    template_name = 'blog/add.html'
    success_url = reverse_lazy('blog:AdminArticle')

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(ArticleCreate, self).dispatch(*args, **kwargs)


class ArticleUpdate(UpdateView):
    model = Article
    form_class = AdminArticleForm
    template_name = 'blog/update.html'
    success_url = reverse_lazy('blog:AdminArticle')

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(ArticleUpdate, self).dispatch(*args, **kwargs)


class ArticleDelete(DeleteView):
    model = Article
    fields = '__all__'
    success_url = reverse_lazy('blog:AdminArticle')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(ArticleDelete, self).dispatch(*args, **kwargs)


#


################# Blog Category##########

class AdminCategoryList(ListView):
    model = Category
    template_name = 'category/admin.html'

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(AdminCategoryList, self).dispatch(*args, **kwargs)


class CategoryDetail(DetailView):
    model = Article
    context_object_name = 'category'
    template_name = 'category/details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(CategoryDetail, self).dispatch(*args, **kwargs)


class CategoryCreate(CreateView):
    model = Category
    # fields = '__all__'
    form_class = AdminArticleCategoryForm
    template_name = 'category/add.html'
    success_url = reverse_lazy('blog:AdminCategory')

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(CategoryCreate, self).dispatch(*args, **kwargs)


class CategoryUpdate(UpdateView):
    model = Category
    form_class = AdminArticleCategoryForm
    template_name = 'category/update.html'
    success_url = reverse_lazy('blog:AdminCategory')

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(CategoryUpdate, self).dispatch(*args, **kwargs)


class CategoryDelete(DeleteView):
    model = Category
    fields = '__all__'
    success_url = reverse_lazy('blog:AdminCategory')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(CategoryDelete, self).dispatch(*args, **kwargs)

    ###################Blog Tag#####################


class AdminTagList(ListView):
    model = Tag
    template_name = 'tag/admin.html'

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(AdminTagList, self).dispatch(*args, **kwargs)


class TagDetail(DetailView):
    model = Tag
    context_object_name = 'tag'
    template_name = 'tag/details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(TagDetail, self).dispatch(*args, **kwargs)


class TagCreate(CreateView):
    model = Tag
    # fields = '__all__'
    form_class = AdminArticleTagTagForm
    template_name = 'tag/add.html'
    success_url = reverse_lazy('blog:AdminTag')

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(TagCreate, self).dispatch(*args, **kwargs)


class TagUpdate(UpdateView):
    model = Tag
    form_class = AdminArticleTagTagForm
    template_name = 'tag/update.html'
    success_url = reverse_lazy('blog:AdminTag')

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(TagUpdate, self).dispatch(*args, **kwargs)


class TagDelete(DeleteView):
    model = Tag
    fields = '__all__'
    success_url = reverse_lazy('blog:AdminTag')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(TagDelete, self).dispatch(*args, **kwargs)
