from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from core.forms.catalog import AdminServicesForm
from core.models.services import Services


##########################      Services Admin            ################################
class ServicesList(ListView):
    model = Services
    template_name = 'services/admin.html'

    # @method_decorator(superuser_only)
    # def dispatch(self, *args, **kwargs):
    #     return super(ServicesList, self).dispatch(*args, **kwargs)


class ServicesDetail(DetailView):
    model = Services
    context_object_name = 'category'
    template_name = 'services/details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    # @method_decorator(superuser_only)
    # def dispatch(self, *args, **kwargs):
    #     return super(ServicesDetail, self).dispatch(*args, **kwargs)


class ServicesCreate(CreateView):
    model = Services
    # fields = '__all__'
    form_class = AdminServicesForm
    template_name = 'services/add.html'
    success_url = reverse_lazy('core:AdminServices')

    # @method_decorator(superuser_only)
    # def dispatch(self, *args, **kwargs):
    #     return super(ServicesCreate, self).dispatch(*args, **kwargs)


class ServicesUpdate(UpdateView):
    model = Services
    form_class = AdminServicesForm
    template_name = 'services/update.html'
    success_url = reverse_lazy('core:AdminServices')

    # @method_decorator(superuser_only)
    # def dispatch(self, *args, **kwargs):
    #     return super(ServicesUpdate, self).dispatch(*args, **kwargs)


class ServicesDelete(DeleteView):
    model = Services
    fields = '__all__'
    success_url = reverse_lazy('core:AdminServices')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    # @method_decorator(superuser_only)
    # def dispatch(self, *args, **kwargs):
    #     return super(ServicesDelete, self).dispatch(*args, **kwargs)
