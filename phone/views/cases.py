from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from lawyer.forms.cases import AdminCasesTypeForm
from lawyer.forms.court import AdminCourtForm
from lawyer.models import Court


##########################      Cases Type Admin            ################################
from lawyer.models.cases import CasesType


class CasesTypeList(ListView):
    model = CasesType
    template_name = 'cases-type/admin.html'

    # @method_decorator(superuser_only)
    # def dispatch(self, *args, **kwargs):
    #     return super(CasesTypeList, self).dispatch(*args, **kwargs)


class CasesTypeDetail(DetailView):
    model = CasesType
    context_object_name = 'type'
    template_name = 'cases-type/details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    # @method_decorator(superuser_only)
    # def dispatch(self, *args, **kwargs):
    #     return super(CasesTypeDetail, self).dispatch(*args, **kwargs)


class CasesTypeCreate(CreateView):
    model = CasesType
    # fields = '__all__'
    form_class = AdminCasesTypeForm
    template_name = 'cases-type/add.html'
    success_url = reverse_lazy('lawyer:AdminCasesType')

    # @method_decorator(superuser_only)
    # def dispatch(self, *args, **kwargs):
    #     return super(CourtCreate, self).dispatch(*args, **kwargs)


class CasesTypeUpdate(UpdateView):
    model = CasesType
    form_class = AdminCasesTypeForm
    template_name = 'cases-type/update.html'
    success_url = reverse_lazy('core:AdminCasesType')

    # @method_decorator(superuser_only)
    # def dispatch(self, *args, **kwargs):
    #     return super(CasesTypeUpdate, self).dispatch(*args, **kwargs)


class CasesTypeDelete(DeleteView):
    model = CasesType
    fields = '__all__'
    success_url = reverse_lazy('core:AdminCasesType')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    # @method_decorator(superuser_only)
    # def dispatch(self, *args, **kwargs):
    #     return super(CasesTypeDelete, self).dispatch(*args, **kwargs)

