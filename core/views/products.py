from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from core.forms.catalog import AdminProductForm, AdminProductSkillsForm, \
    AdminFeaturesForm
from core.models.services import Products, Features, ProductSkills, Categories


##########################      OurWork Admin            ################################
class ProductList(ListView):
    model = Products
    template_name = 'products/admin.html'

    # @method_decorator(superuser_only)
    # def dispatch(self, *args, **kwargs):
    #     return super(ProductList, self).dispatch(*args, **kwargs)


class ProductDetail(DetailView):
    model = Products
    context_object_name = 'category'
    template_name = 'products/details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    # @method_decorator(superuser_only)
    # def dispatch(self, *args, **kwargs):
    #     return super(ProductDetail, self).dispatch(*args, **kwargs)


#
# @login_required(login_url='/dashboard/login')
# @superuser_only
def ProductAdd(request):  # sourcery skip: aug-assign, convert-to-enumerate
    features = Features.objects.all()
    product_skills = ProductSkills.objects.all()
    category = Categories.objects.all()
    if request.method == "POST":
        print(request)
        product_form = AdminProductForm(request.POST or None, request.FILES or None)
        features_form = AdminFeaturesForm(request.POST or None, request.FILES or None)
        skills_form = AdminProductSkillsForm(request.POST or None, request.FILES or None)
        if product_form.is_valid() and features_form.is_valid() and skills_form.is_valid():
            print(request.POST)
            product_created = True
            title = product_form.cleaned_data['title']
            keyword = product_form.cleaned_data['keyword']
            category = product_form.cleaned_data['category']
            is_featured = product_form.cleaned_data['is_featured']
            long_desc = product_form.cleaned_data['long_desc']
            image = request.FILES.get('image')
            project_name = product_form.cleaned_data['project_name']
            project_type = product_form.cleaned_data['project_type']
            skills = product_form.cleaned_data['skills']
            demo = product_form.cleaned_data['demo']
            files = request.FILES.get('files')
            pdf = request.FILES.get('pdf')
            cloud_file = product_form.cleaned_data['cloud_file']
            tags = product_form.cleaned_data['tags']
            brand = product_form.cleaned_data['brand']
            status = product_form.cleaned_data['status']
            sort_order = product_form.cleaned_data['sort_order']
            slug = product_form.cleaned_data['slug']
            ############## Features ###########
            features_titles = request.POST.getlist('features_title')
            features_keyword = request.POST.getlist('features_keyword')
            features_category = request.POST.getlist('features_category')
            features_name = request.POST.getlist('features_name')
            features_description = request.POST.getlist('features_description')
            icon = request.FILES.getlist('icon')
            ############## Skills ###########
            product_skills = request.POST.getlist('product_skill')
            percentage = request.POST.getlist('percentage')
            category = Categories.objects.get(title=category)
            product_form = None
            if not product_form:
                print(request)
                print(request.POST)
                product_form = Products(title=title, keyword=keyword, category=category, is_featured=is_featured,
                                        long_desc=long_desc, image=image, project_name=project_name,
                                        project_type=project_type,
                                        skills=skills, demo=demo, files=files, pdf=pdf, cloud_file=cloud_file,
                                        tags=tags, brand=brand,
                                        status=status, sort_order=sort_order, slug=slug)
                product_form.save()
                a = 0
                for features_title in features_titles:
                    features_categories = Categories.objects.get(id=features_category[a])

                    features_form = Features(product=product_form, features_title=features_title,
                                             features_keyword=features_keyword[a],
                                             features_category=features_categories, features_name=features_name[a],
                                             features_description=features_description[a], icon=icon[a])
                    features_form.save()
                    a = a + 1
                c = 0
                for product_skill in product_skills:
                    skills_form = ProductSkills(product=product_form, product_skill=product_skill,
                                                percentage=percentage[c])
                    skills_form.save()
                    c = c + 1
                    print(request.POST)
                    # use django messages framework
                messages.success(request,
                                 "Yeeew, check it out on the home page!")
                return HttpResponseRedirect(reverse_lazy('core:AdminProduct'))
            else:
                print("Form invalid, see below error msg")
                print(request.POST)
                messages.error(request, "Error")
    else:
        product_form = AdminProductForm()
        features_form = AdminFeaturesForm()
        skills_form = AdminProductSkillsForm()
        context = {
            'features': features,
            'product_skills': product_skills,
            'category': category,
            'product_form': product_form,
            'features_form': features_form,
            'skills_form': skills_form,
        }
        return render(request, 'products/add.html', context)
    context = {
        'features': features,
        'product_skills': product_skills,
        'category': category,
        'product_form': product_form,
        'features_form': features_form,
        'skills_form': skills_form,
    }
    return render(request, 'products/add.html', context)


class ProductCreate(CreateView):
    model = Products
    # fields = '__all__'
    form_class = AdminProductForm
    template_name = 'products/add.html'
    success_url = reverse_lazy('core:AdminProduct')

    # @method_decorator(superuser_only)
    # def dispatch(self, *args, **kwargs):
    #     return super(ProductCreate, self).dispatch(*args, **kwargs)


class ProductUpdate(UpdateView):
    model = Products
    form_class = AdminProductForm
    template_name = 'products/update.html'
    success_url = reverse_lazy('core:AdminProduct')

    # @method_decorator(superuser_only)
    # def dispatch(self, *args, **kwargs):
    #     return super(ProductUpdate, self).dispatch(*args, **kwargs)


class ProductDelete(DeleteView):
    model = Products
    fields = '__all__'
    template_name = 'confirm_delete.html'

    success_url = reverse_lazy('core:AdminProduct')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    # @method_decorator(superuser_only)
    # def dispatch(self, *args, **kwargs):
    #     return super(ProductDelete, self).dispatch(*args, **kwargs)
