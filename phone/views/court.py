from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from lawyer.forms.court import AdminCourtForm, AdminCourtCircuitForm
from lawyer.models import Court, CourtCircuit


##########################      Services Admin            ################################
class CourtList(ListView):
    model = Court
    template_name = 'court/admin.html'

    # @method_decorator(superuser_only)
    # def dispatch(self, *args, **kwargs):
    #     return super(CourtList, self).dispatch(*args, **kwargs)


class CourtDetail(DetailView):
    model = Court
    context_object_name = 'court'
    template_name = 'court/details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    # @method_decorator(superuser_only)
    # def dispatch(self, *args, **kwargs):
    #     return super(CourtDetail, self).dispatch(*args, **kwargs)


class CourtCreate(CreateView):
    model = Court
    # fields = '__all__'
    form_class = AdminCourtForm
    template_name = 'court/add.html'
    success_url = reverse_lazy('lawyer:AdminCourt')

    # @method_decorator(superuser_only)
    # def dispatch(self, *args, **kwargs):
    #     return super(CourtCreate, self).dispatch(*args, **kwargs)


class CourtUpdate(UpdateView):
    model = Court
    form_class = AdminCourtForm
    template_name = 'court/update.html'
    success_url = reverse_lazy('core:AdminCourt')

    # @method_decorator(superuser_only)
    # def dispatch(self, *args, **kwargs):
    #     return super(CourtUpdate, self).dispatch(*args, **kwargs)


class CourtDelete(DeleteView):
    model = Court
    fields = '__all__'
    success_url = reverse_lazy('core:AdminCourt')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    # @method_decorator(superuser_only)
    # def dispatch(self, *args, **kwargs):
    #     return super(CourtDelete, self).dispatch(*args, **kwargs)


##########################      Court Circuit Admin            ################################
class CourtCircuitList(ListView):
    model = CourtCircuit
    template_name = 'court-circuit/admin.html'

    # @method_decorator(superuser_only)
    # def dispatch(self, *args, **kwargs):
    #     return super(CourtCircuitList, self).dispatch(*args, **kwargs)


class CourtCircuitDetail(DetailView):
    model = CourtCircuit
    context_object_name = 'circuit'
    template_name = 'court-circuit/details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    # @method_decorator(superuser_only)
    # def dispatch(self, *args, **kwargs):
    #     return super(CourtCircuitDetail, self).dispatch(*args, **kwargs)


class CourtCircuitCreate(CreateView):
    model = CourtCircuit
    # fields = '__all__'
    form_class = AdminCourtCircuitForm
    template_name = 'court-circuit/add.html'
    success_url = reverse_lazy('lawyer:AdminCourtCircuit')

    # @method_decorator(superuser_only)
    # def dispatch(self, *args, **kwargs):
    #     return super(CourtCircuitCreate, self).dispatch(*args, **kwargs)





class CourtCircuitUpdate(UpdateView):
    model = CourtCircuit
    form_class = AdminCourtCircuitForm
    template_name = 'court-circuit/update.html'
    success_url = reverse_lazy('lawyer:AdminCourtCircuit')

    # @method_decorator(superuser_only)
    # def dispatch(self, *args, **kwargs):
    #     return super(CourtCircuitUpdate, self).dispatch(*args, **kwargs)


class CourtCircuitDelete(DeleteView):
    model = CourtCircuit
    fields = '__all__'
    success_url = reverse_lazy('lawyer:AdminCourtCircuit')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    # @method_decorator(superuser_only)
    # def dispatch(self, *args, **kwargs):
    #     return super(CourtCircuitDelete, self).dispatch(*args, **kwargs)