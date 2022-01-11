from billing.models.models import CommissionSystem, ShippingZone, ShippingCategory, ShippingRate
from core.forms.billing import AdminShippingZoneForm, AdminShippingCategoryForm, AdminShippingRateForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView, CreateView, ListView, DeleteView

from core.decorators import superuser_only


class CommissionSystemList(ListView):
    model = CommissionSystem
    template_name = 'sales/commission/admin-commission.html'


class CommissionSystemCreate(CreateView):
    model = CommissionSystem
    fields = '__all__'
    # form_class = PaymentMethodsForm
    template_name = 'sales/commission/add-commission.html'
    success_url = reverse_lazy('core:AdminCommissionSystemList')

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(CommissionSystemCreate, self).dispatch(*args, **kwargs)


class CommissionSystemUpdate(UpdateView):
    model = CommissionSystem
    fields = '__all__'
    template_name = 'sales/commission/edit-commission.html'
    success_url = reverse_lazy('core:AdminCommissionSystemList')

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(CommissionSystemUpdate, self).dispatch(*args, **kwargs)


class CommissionSystemDelete(DeleteView):
    model = CommissionSystem
    fields = '__all__'
    success_url = reverse_lazy('core:AdminCommissionSystemList')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)


############################SHIPPING Zone##################

class AdminShippingZoneList(ListView):
    model = ShippingZone
    template_name = 'sales/billing/ShippingZone/admin-shippingzone.html'


class AdminShippingZoneCreate(CreateView):
    model = ShippingZone

    form_class = AdminShippingZoneForm
    template_name = 'sales/billing/ShippingZone/add-shippingzone.html'
    success_url = reverse_lazy('core:AdminShippingZoneList')

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(AdminShippingZoneCreate, self).dispatch(*args, **kwargs)


class AdminShippingZoneUpdate(UpdateView):
    model = ShippingZone
    form_class = AdminShippingZoneForm
    template_name = 'sales/billing/ShippingZone/edit-shippingzone.html'
    success_url = reverse_lazy('core:AdminShippingZoneList')

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(AdminShippingZoneUpdate, self).dispatch(*args, **kwargs)


class AdminShippingZoneDelete(DeleteView):
    model = ShippingZone
    fields = '__all__'
    success_url = reverse_lazy('core:AdminShippingZoneList')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)


############################SHIPPING Category ##################

class AdminShippingCategoryList(ListView):
    model = ShippingCategory
    template_name = 'sales/billing/ShippingCategory/admin-shippingcategory.html'


class AdminShippingCategoryCreate(CreateView):
    model = ShippingCategory

    form_class = AdminShippingCategoryForm
    template_name = 'sales/billing/ShippingCategory/add-shippingcategory.html'
    success_url = reverse_lazy('core:AdminShippingCategoryList')

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(AdminShippingCategoryCreate, self).dispatch(*args, **kwargs)


class AdminShippingCategoryUpdate(UpdateView):
    model = ShippingCategory
    form_class = AdminShippingCategoryForm
    template_name = 'sales/billing/ShippingCategory/edit-shippingcategory.html'
    success_url = reverse_lazy('core:AdminShippingCategoryList')

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(AdminShippingCategoryUpdate, self).dispatch(*args, **kwargs)


class AdminShippingCategoryDelete(DeleteView):
    model = ShippingCategory
    fields = '__all__'
    success_url = reverse_lazy('core:AdminShippingCategoryList')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)


############################SHIPPING Rate##################

class AdminShippingRateList(ListView):
    model = ShippingRate
    template_name = 'sales/billing/ShippingRate/admin-shippingrate.html'


class AdminShippingRateCreate(CreateView):
    model = ShippingRate

    form_class = AdminShippingRateForm
    template_name = 'sales/billing/ShippingRate/add-shippingrate.html'
    success_url = reverse_lazy('core:AdminShippingRateList')

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(AdminShippingRateCreate, self).dispatch(*args, **kwargs)


class AdminShippingRateUpdate(UpdateView):
    model = ShippingRate
    form_class = AdminShippingRateForm
    template_name = 'sales/billing/ShippingRate/edit-shippingrate.html'
    success_url = reverse_lazy('core:AdminShippingRateList')

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(AdminShippingRateUpdate, self).dispatch(*args, **kwargs)


class AdminShippingRateDelete(DeleteView):
    model = ShippingRate
    fields = '__all__'
    success_url = reverse_lazy('core:AdminShippingRateList')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)
