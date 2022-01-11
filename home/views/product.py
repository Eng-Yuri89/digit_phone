from django.shortcuts import render
from django.utils import timezone
from django.views.generic import ListView, DetailView

from core.models.services import Services, Products


def test(request):
    return render(request, 'front/product/product-details.html', )


##########################      Services Admin            ################################
class ServicesList(ListView):
    model = Services
    template_name = 'front/product/product-details.html'


class ProductDetail(DetailView):
    model = Products
    context_object_name = 'product'
    template_name = 'front/product/product-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
