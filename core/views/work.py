from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from core.forms.catalog import AdminCategoryForm, AdminWorkForm
from core.models.services import OurWork


##########################      OurWork Admin            ################################
class OurWorkList(ListView):
    model = OurWork
    template_name = 'work/admin.html'

    # @method_decorator(superuser_only)
    # def dispatch(self, *args, **kwargs):
    #     return super(OurWorkList, self).dispatch(*args, **kwargs)


class OurWorkDetail(DetailView):
    model = OurWork
    context_object_name = 'category'
    template_name = 'work/details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    # @method_decorator(superuser_only)
    # def dispatch(self, *args, **kwargs):
    #     return super(OurWorkDetail, self).dispatch(*args, **kwargs)


class OurWorkCreate(CreateView):
    model = OurWork
    # fields = '__all__'
    form_class = AdminWorkForm
    template_name = 'work/add.html'
    success_url = reverse_lazy('core:AdminCategory')

    # @method_decorator(superuser_only)
    # def dispatch(self, *args, **kwargs):
    #     return super(OurWorkCreate, self).dispatch(*args, **kwargs)


class OurWorkUpdate(UpdateView):
    model = OurWork
    form_class = AdminCategoryForm
    template_name = 'work/update.html'
    success_url = reverse_lazy('core:AdminCategory')

    # @method_decorator(superuser_only)
    # def dispatch(self, *args, **kwargs):
    #     return super(OurWorkUpdate, self).dispatch(*args, **kwargs)


class OurWorkDelete(DeleteView):
    model = OurWork
    fields = '__all__'
    success_url = reverse_lazy('core:AdminCategory')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    # @method_decorator(superuser_only)
    # def dispatch(self, *args, **kwargs):
    #     return super(CategoriesDelete, self).dispatch(*args, **kwargs)
