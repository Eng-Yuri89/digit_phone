from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.http import request, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView, DetailView, DeleteView, CreateView, UpdateView, ListView

from core.decorators import superuser_only
from core.forms.design import BannersAddForm, SliderAddForm
from core.models.design import Slider, SliderMedia, Banners


class SliderView(TemplateView):
    template_name = "design/slider/admin.html"
    paginate_by = 10  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sliders'] = Slider.objects.all()
        return context

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(SliderView, self).dispatch(*args, **kwargs)


class SliderDetailView(DetailView):
    model = Slider
    context_object_name = 'slider'
    template_name = 'design/slider/update.html'

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(SliderDetailView, self).dispatch(*args, **kwargs)


class SliderDelete(DeleteView):
    model = Slider
    fields = '__all__'
    success_url = reverse_lazy('core:AdminSlider')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(SliderDelete, self).dispatch(*args, **kwargs)


class SliderCreate(View):
    def get(self, request, *args, **kwargs):
        slider = Slider.objects.all()

        return render(request, "design/slider/add.html",
                      {"groups": slider, })

    print(request)

    def post(self, request, *args, **kwargs):
        title = request.POST.get("title")
        group = request.POST.get("group")
        status = request.POST.get("status")
        sort_order = request.POST.get("sort_order")
        media_type_list = request.POST.getlist("media_type[]")
        media_content_list = request.FILES.getlist("media_content[]")
        media_link_list = request.POST.getlist("media_link[]")

        print(request.POST)

        # status = request.POST.get("status")

        slider = Slider(title=title, group=group, status=status, sort_order=sort_order,
                        )
        slider.save()

        i = 0
        for media_content in media_content_list:
            fs = FileSystemStorage()
            filename = fs.save(media_content.name, media_content)
            media_url = fs.url(filename)
            slider_media = SliderMedia(slider_id=slider, media_type=media_type_list[i],
                                       media_link=media_link_list[i], media_content=media_url)
            slider_media.save()
            i = i + 1

        # return HttpResponse("OK")
        return HttpResponseRedirect(reverse_lazy('core:AdminSliderView'))

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(SliderCreate, self).dispatch(*args, **kwargs)


class SliderEdit(UpdateView):
    model = Slider
    form_class = SliderAddForm
    template_name = 'design/slider/update.html'
    success_url = reverse_lazy('core:AdminSliderView')

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(SliderEdit, self).dispatch(*args, **kwargs)


###################Banners#############

class BannersView(ListView):
    model = Banners
    template_name = "design/banner/admin.html"
    paginate_by = 10  # if pagination is desired

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(BannersView, self).dispatch(*args, **kwargs)


class BannerDetailView(DetailView):
    model = Banners
    context_object_name = 'design'
    template_name = 'design/banner/details.html'

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(BannerDetailView, self).dispatch(*args, **kwargs)


class BannerDelete(DeleteView):
    model = Banners
    fields = '__all__'
    success_url = reverse_lazy('core:AdminBanner')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(BannerDelete, self).dispatch(*args, **kwargs)


@login_required(login_url='/dashboard/login')
@superuser_only
def BannerCreate(request):  # sourcery skip: aug-assign, convert-to-enumerate

    if request.method == "POST":
        print(request)

        banner_form = BannersAddForm(request.POST or None, request.FILES or None)

        if banner_form.is_valid():
            return _extracted_from_BannerCreate_10(request, banner_form)
        print("Form invalid, see below error msg")
        print(request.POST)
        messages.error(request, "Error")

    else:
        banner_form = BannersAddForm()
    # return redirect(reverse('core:ProductAdd'))

    return render(request, 'design/banner/add.html',
                  {'banner_form': banner_form, }
                  )


def _extracted_from_BannerCreate_10(request, banner_form):
    print(request.POST)
    product_created = True
    position = banner_form.cleaned_data['position']
    status = banner_form.cleaned_data['status']

    media_content = banner_form.cleaned_data['media_content']
    media_link = banner_form.cleaned_data['media_link']

    banner_form = None
    if not banner_form:
        print(request)
        print(request.POST)

        banner_form = Banners(position=position, status=status,
                              media_content=media_content, media_link=media_link,
                              )

        banner_form.save()

        print(request.POST)
        # use django messages framework
    messages.success(request,
                     "Yeeew, check it out on the home page!")

    return HttpResponseRedirect(reverse_lazy('core:AdminBannerView'))


class BannerEdit(UpdateView):
    model = Banners
    form_class = BannersAddForm
    template_name = 'design/banner/update.html'
    success_url = reverse_lazy('core:AdminBannerView')

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(BannerEdit, self).dispatch(*args, **kwargs)



