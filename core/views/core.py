# @admin_required
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.models import Article
from core.decorators import superuser_only
#
# @login_required(login_url='/dashboard/login')
# @superuser_only
from core.forms.catalog import AdminCategoryForm, AdminTagsForm
from core.models.design import Setting
from core.models.services import Categories, Tags, Products


@login_required(login_url='/dashboard/login')
@superuser_only
def AdminIndex(request):
    categories = Categories.objects.all()
    try:
        admin_products_count = Products.objects.all().count()
        need_active = Setting.objects.filter(status=True)
        article_view = Article.objects.filter(status='Publish', ).aggregate(TOTAL=Sum('views'))['TOTAL']


    except Exception as e:
        return {

            'admin_orders_location': None,

        }

    context = {
        'categories': categories,
        'admin_products_count': admin_products_count,
        'need_active': need_active,
        'article_view': article_view,

        # 'products': products,
        # 'catalog': Products,
        # 'vendor': store,
        # 'setting': setting,
        # 'index_language': index_language

    }



    return render(request, 'backend/index.html', )


##########################      Category Admin            ################################
class CategoryList(ListView):
    model = Categories
    template_name = 'catalog/category/admin.html'

    # @method_decorator(superuser_only)
    # def dispatch(self, *args, **kwargs):
    #     return super(CategoryList, self).dispatch(*args, **kwargs)


class CategoriesDetail(DetailView):
    model = Categories
    context_object_name = 'category'
    template_name = 'catalog/category/details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    # @method_decorator(superuser_only)
    # def dispatch(self, *args, **kwargs):
    #     return super(CategoriesDetail, self).dispatch(*args, **kwargs)


class CategoriesCreate(CreateView):
    model = Categories
    # fields = '__all__'
    form_class = AdminCategoryForm
    template_name = 'catalog/category/add.html'
    success_url = reverse_lazy('core:AdminCategory')

    # @method_decorator(superuser_only)
    # def dispatch(self, *args, **kwargs):
    #     return super(CategoriesCreate, self).dispatch(*args, **kwargs)


class CategoriesUpdate(UpdateView):
    model = Categories
    form_class = AdminCategoryForm
    template_name = 'catalog/category/update.html'
    success_url = reverse_lazy('core:AdminCategory')

    # @method_decorator(superuser_only)
    # def dispatch(self, *args, **kwargs):
    #     return super(CategoriesUpdate, self).dispatch(*args, **kwargs)


class CategoriesDelete(DeleteView):
    model = Categories
    fields = '__all__'
    success_url = reverse_lazy('core:AdminCategory')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    # @method_decorator(superuser_only)
    # def dispatch(self, *args, **kwargs):
    #     return super(CategoriesDelete, self).dispatch(*args, **kwargs)


##########################      Tags            ################################


class TagsList(ListView):
    model = Tags
    template_name = 'catalog/tags/admin.html'

    # @method_decorator(superuser_only)
    # def dispatch(self, *args, **kwargs):
    #     return super(TagsList, self).dispatch(*args, **kwargs)


class TagsDetail(DetailView):
    model = Categories
    context_object_name = 'tags'
    template_name = 'catalog/tags/details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(TagsDetail, self).dispatch(*args, **kwargs)


class TagsCreate(CreateView):
    model = Tags
    # fields = '__all__'
    form_class = AdminTagsForm
    template_name = 'catalog/tags/add.html'
    success_url = reverse_lazy('core:AdminTags')

    # @method_decorator(superuser_only)
    # def dispatch(self, *args, **kwargs):
    #     return super(TagsCreate, self).dispatch(*args, **kwargs)


class TagsUpdate(UpdateView):
    model = Tags
    form_class = AdminTagsForm
    template_name = 'catalog/tags/update.html'
    success_url = reverse_lazy('core:AdminTags')

    # @method_decorator(superuser_only)
    # def dispatch(self, *args, **kwargs):
    #     return super(TagsUpdate, self).dispatch(*args, **kwargs)


class TagsDelete(DeleteView):
    model = Categories
    fields = '__all__'
    success_url = reverse_lazy('core:AdminTags')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(TagsDelete, self).dispatch(*args, **kwargs)
