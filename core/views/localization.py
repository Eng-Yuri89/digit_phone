from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from core.models.localization import Country, Governorates, City, Area, Language, Currency

from core.decorators import superuser_only
from core.forms.localization import AdminCountryForm, AdminCurrencyForm, AdminLanguageForm, AdminCityForm, \
    AdminAreaForm, AdminGovernoratesForm


class LanguageListView(ListView):
    model = Language

    template_name = 'localization/language/admin-language.html'
    paginate_by = 10  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['title'] = 'Country'
        return context

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(LanguageListView, self).dispatch(*args, **kwargs)


class LanguageCreate(CreateView):
    model = Language
    form_class = AdminLanguageForm
    template_name = 'localization/language/add-language.html'
    success_url = reverse_lazy('core:LanguageListView')

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(LanguageCreate, self).dispatch(*args, **kwargs)


class LanguageEdit(UpdateView):
    model = Language
    form_class = AdminLanguageForm
    template_name = 'localization/language/edit-language.html'
    success_url = reverse_lazy('core:LanguageListView')

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(LanguageEdit, self).dispatch(*args, **kwargs)


class LanguageDelete(DeleteView):
    model = Language
    fields = '__all__'
    success_url = reverse_lazy('core:AdminLanguageListView')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(LanguageDelete, self).dispatch(*args, **kwargs)


############Currency############
class CurrencyListView(ListView):
    model = Currency

    template_name = 'localization/currency/admin-currency.html'
    paginate_by = 10  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['title'] = 'Country'
        return context

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(CurrencyListView, self).dispatch(*args, **kwargs)


class CurrencyDetailView(DetailView):
    model = Currency

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(CurrencyDetailView, self).dispatch(*args, **kwargs)


class CurrencyCreate(CreateView):
    model = Currency
    form_class = AdminCurrencyForm
    template_name = 'localization/currency/add-currency.html'
    success_url = reverse_lazy('core:AdminCurrencyListView')

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(CurrencyCreate, self).dispatch(*args, **kwargs)


class CurrencyEdit(UpdateView):
    model = Currency
    form_class = AdminCurrencyForm
    template_name = 'localization/currency/edit-currency.html'
    success_url = reverse_lazy('core:AdminCurrencyListView')

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(CurrencyEdit, self).dispatch(*args, **kwargs)


class CurrencyDelete(DeleteView):
    model = Currency
    fields = '__all__'
    success_url = reverse_lazy('core:AdminCurrencyListView')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(CurrencyDelete, self).dispatch(*args, **kwargs)


############Country############


class CountryListView(ListView):
    model = Country

    template_name = 'localization/country/admin.html'
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['title'] = 'Country'
        return context

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(CountryListView, self).dispatch(*args, **kwargs)


class CountryDetailView(DetailView):
    model = Country

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(CountryDetailView, self).dispatch(*args, **kwargs)


class CountryCreate(CreateView):
    model = Country
    form_class = AdminCountryForm
    template_name = 'localization/country/add.html'
    success_url = reverse_lazy('core:AdminCountryListView')

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(CountryCreate, self).dispatch(*args, **kwargs)


class CountryEdit(UpdateView):
    model = Country
    fields = '__all__'
    template_name = 'localization/country/update.html'
    success_url = reverse_lazy('core:AdminCountryListView')

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(CountryEdit, self).dispatch(*args, **kwargs)


class CountryDelete(DeleteView):
    model = Country
    fields = '__all__'
    success_url = reverse_lazy('core:AdminCountryListView')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(CountryDelete, self).dispatch(*args, **kwargs)


####################Governorates#################

class GovernoratesListView(ListView):
    model = Governorates
    template_name = 'localization/governorate/admin.html'
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(GovernoratesListView, self).dispatch(*args, **kwargs)


class GovernoratesDetailView(DetailView):
    model = Governorates

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(GovernoratesDetailView, self).dispatch(*args, **kwargs)


class GovernoratesCreate(CreateView):
    model = Governorates
    form_class = AdminGovernoratesForm
    template_name = 'localization/governorate/add.html'
    success_url = reverse_lazy('core:AdminGovernoratesListView')

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(GovernoratesCreate, self).dispatch(*args, **kwargs)


class GovernoratesEdit(UpdateView):
    model = Governorates
    fields = '__all__'
    template_name = 'localization/governorate/update.html'
    success_url = reverse_lazy('core:AdminGovernoratesListView')

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(GovernoratesEdit, self).dispatch(*args, **kwargs)


class GovernoratesDelete(DeleteView):
    model = Governorates
    fields = '__all__'
    success_url = reverse_lazy('core:AdminGovernoratesListView')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(GovernoratesDelete, self).dispatch(*args, **kwargs)


##################CIty##############
class CityListView(ListView):
    model = City
    template_name = 'localization/city/admin.html'
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(CityListView, self).dispatch(*args, **kwargs)


class CityDetailView(DetailView):
    model = City

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(CityDetailView, self).dispatch(*args, **kwargs)


class CityCreate(CreateView):
    model = City
    form_class = AdminCityForm
    template_name = 'localization/city/add.html'
    success_url = reverse_lazy('core:AdminCityListView')

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(CityCreate, self).dispatch(*args, **kwargs)


class CityEdit(UpdateView):
    model = City
    fields = '__all__'
    template_name = 'localization/city/update.html'
    success_url = reverse_lazy('core:AdminCityListView')

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(CityEdit, self).dispatch(*args, **kwargs)


class CityDelete(DeleteView):
    model = City
    fields = '__all__'
    success_url = reverse_lazy('core:AdminCityListView')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(CityDelete, self).dispatch(*args, **kwargs)


##################Area##############
class AreaListView(ListView):
    model = Area
    template_name = 'localization/area/admin.html'
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(AreaListView, self).dispatch(*args, **kwargs)


class AreaDetailView(DetailView):
    model = Area

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(AreaDetailView, self).dispatch(*args, **kwargs)


class AreaCreate(CreateView):
    model = Area
    form_class = AdminAreaForm
    template_name = 'localization/area/add.html'
    success_url = reverse_lazy('core:AdminAreaListView')

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(AreaCreate, self).dispatch(*args, **kwargs)


class AreaEdit(UpdateView):
    model = City
    fields = '__all__'
    template_name = 'localization/area/update.html'
    success_url = reverse_lazy('core:AdminAreaListView')

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(AreaEdit, self).dispatch(*args, **kwargs)


class AreaDelete(DeleteView):
    model = Area
    fields = '__all__'
    success_url = reverse_lazy('core:AdminAreaListView')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(AreaDelete, self).dispatch(*args, **kwargs)
