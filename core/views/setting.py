from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DeleteView, DetailView

from core.decorators import superuser_only
# Create your views here.
from core.forms.setting import AdminSettingForm, AdminExtraSettingForm, AdminSettingSkillsForm, \
    AdminSettingFeaturesForm, AdminSeoSettingForm
from core.models.design import Setting, ExtraSetting, SeoSetting, SettingFeatures, SettingSkills


class AdminSetting(ListView):
    model = Setting

    template_name = 'setting/admin.html'

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(AdminSetting, self).dispatch(*args, **kwargs)


class AdminSettingDetail(DetailView):
    model = Setting
    context_object_name = 'setting'
    template_name = 'setting/details.html'


@login_required(login_url='/dashboard/login')
@superuser_only
def AdminAddSetting(request, ):
    if request.method == "POST":
        setting_form = AdminSettingForm(request.POST or None, request.FILES or None)
        extra_form = AdminExtraSettingForm(request.POST or None, request.FILES or None)
        seo_form = AdminSeoSettingForm(request.POST or None, request.FILES or None)
        features_form = AdminSettingFeaturesForm(request.POST or None, request.FILES or None)
        skills_form = AdminSettingSkillsForm(request.POST or None, request.FILES or None)
        print(request)
        if setting_form.is_valid() and extra_form.is_valid() and seo_form.is_valid() \
                and features_form.is_valid() and skills_form.is_valid():

            print(request.POST)
            product_created = True
            title = setting_form.cleaned_data['title']
            keywords = setting_form.cleaned_data['keywords']
            copyright = setting_form.cleaned_data['copyright']
            email = setting_form.cleaned_data['email']
            image = setting_form.cleaned_data['image']
            facebook = setting_form.cleaned_data['facebook']
            instagram = setting_form.cleaned_data['instagram']
            twitter = setting_form.cleaned_data['twitter']
            linkedin = setting_form.cleaned_data['linkedin']
            behance = setting_form.cleaned_data['behance']
            youtube = setting_form.cleaned_data['youtube']
            status = setting_form.cleaned_data['status']
            slug = setting_form.cleaned_data['slug']
            #########ExtraSetting####
            phone = extra_form.cleaned_data['phone']
            country = extra_form.cleaned_data['country']
            address = extra_form.cleaned_data['address']
            about = extra_form.cleaned_data['about']
            contact = extra_form.cleaned_data['contact']
            extra_keywords = extra_form.cleaned_data['extra_keywords']
            #########Seo Setting####
            seo_description = seo_form.cleaned_data['seo_description']
            seo_author = seo_form.cleaned_data['seo_author']
            seo_keywords = seo_form.cleaned_data['seo_keywords']
            seo_title = seo_form.cleaned_data['seo_title']
            seo_image = request.FILES.get('seo_image')
            seo_site_name = seo_form.cleaned_data['seo_site_name']
            # features#######
            features_titles = request.POST.getlist('features_title')
            features_keyword = request.POST.getlist('features_keyword')
            icon = request.FILES.getlist('icon')
            ###skill#############
            setting_skills = request.POST.getlist('setting_skill')
            percentage = request.POST.getlist('percentage')
            setting_form = None
            if not setting_form:
                print(request)
                print(request.POST)
                setting_form = Setting(title=title, keywords=keywords, copyright=copyright, email=email, image=image,
                                       facebook=facebook, instagram=instagram, twitter=twitter, linkedin=linkedin,
                                       behance=behance, youtube=youtube, status=status, slug=slug)
                setting_form.save()
                extra_form = ExtraSetting(setting=setting_form, phone=phone, country=country,
                                          address=address, about=about, contact=contact, extra_keywords=extra_keywords)
                extra_form.save()
                seo_form = SeoSetting(setting=setting_form, seo_description=seo_description, seo_author=seo_author,
                                      seo_keywords=seo_keywords, seo_title=seo_title, seo_image=seo_image,
                                      seo_site_name=seo_site_name)
                seo_form.save()
                a = 0
                for features_title in features_titles:
                    features_form = SettingFeatures(setting=setting_form, features_title=features_title,
                                                    features_keyword=features_keyword[a], icon=icon[a])
                    features_form.save()
                    a = a + 1
                c = 0
                for setting_skill in setting_skills:
                    skills_form = SettingSkills(setting=setting_form, setting_skill=setting_skill,
                                                percentage=percentage[c])
                    skills_form.save()
                    c = c + 1
                    print(request.POST)
                    # use django messages framework
                messages.success(request,
                                 "Yeeew, check it out on the home page!")
                return HttpResponseRedirect(reverse_lazy('core:AdminSetting'))
            else:
                print("Form invalid, see below error msg")
                print(request.POST)
                messages.error(request, "Error")
    else:
        setting_form = AdminSettingForm()

        extra_form = AdminExtraSettingForm()
        seo_form = AdminSeoSettingForm()
        features_form = AdminSettingFeaturesForm()
        skills_form = AdminSettingSkillsForm()
        context = {
            'setting_form': setting_form,

            'extra_form': extra_form,
            'seo_form': seo_form,
            'features_form': features_form,
            'skills_form': skills_form,
        }
        return render(request, 'setting/add.html', context)
    context = {
        'setting_form': setting_form,

        'extra_form': extra_form,
        'seo_form': seo_form,
        'features_form': features_form,
        'skills_form': skills_form,
    }
    return render(request, 'setting/add.html', context)


class SettingDelete(DeleteView):
    model = Setting
    fields = '__all__'
    success_url = reverse_lazy('core:AdminSetting')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    @method_decorator(superuser_only)
    def dispatch(self, *args, **kwargs):
        return super(SettingDelete, self).dispatch(*args, **kwargs)
