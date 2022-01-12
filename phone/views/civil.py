import json

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from lawyer.forms.cases import AdminCasesTypeForm, AdminCivilCasesTypeForm, AdminClientCasesTypeForm
from lawyer.forms.court import AdminCourtForm
from lawyer.models import Court, Client

##########################      Cases Type Admin            ################################
from lawyer.models.cases import CasesType, Cases


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



class CasesTypeCreate(CreateView):
    model = CasesType
    # fields = '__all__'
    form_class = AdminCasesTypeForm
    template_name = 'cases-type/add.html'
    success_url = reverse_lazy('lawyer:AdminCasesType')

    # @method_decorator(superuser_only)
    # def dispatch(self, *args, **kwargs):
    #     return super(CourtCreate, self).dispatch(*args, **kwargs)


@login_required(login_url='/dashboard/login')
# @superuser_only
def civil_create(request):  # sourcery skip: aug-assign, convert-to-enumerate
    client = Client.objects.all()

    if request.method == "POST":
        print(request)
        civil_form = AdminCivilCasesTypeForm(request.POST or None, request.FILES or None)
        client_form = AdminClientCasesTypeForm(request.POST or None, request.FILES or None)
        if civil_form.is_valid():
            print(request.POST)
            attorney_created = True
            client = request.POST.get('client')
            client_code = request.POST.get('client_code')
            client_type = request.POST.get('client_type')
            national_id = request.POST.get('national_id')
            attorney_number = request.POST.get('attorney_number')
            attorney_code = request.POST.get('attorney_code')
            extraction_place = request.POST.get('extraction_place')
            extraction_date = request.POST.get('extraction_date')
            image = request.FILES.get('image')
            file = request.FILES.get('file')

            client_id = Client.objects.get(client=client)
            attorney_form = None
            if not attorney_form:
                print(request)
                print(request.POST)
                attorney_form = Cases(client=client_id, client_code=client_code, client_type=client_type,
                                         national_id=national_id, attorney_number=attorney_number,
                                         attorney_code=attorney_code,
                                         extraction_place=extraction_place, extraction_date=extraction_date,
                                         image=image, file=file)
                attorney_form.save()

                messages.success(request,
                                 "Yeeew, check it out on the home page!")
                return HttpResponseRedirect(reverse_lazy('lawyer:AdminAttorney'))
            else:
                print("Form invalid, see below error msg")
                print(request.POST)
                messages.error(request, "Error")
    else:
        civil_form = AdminCivilCasesTypeForm()
        client_form = AdminClientCasesTypeForm()
        context = {

            'client': client,
            'civil_form': civil_form,
            'client_form': client_form,

        }
        return render(request, 'cases/civil-add.html', context)
    context = {
        'client': client,
        'civil_form': civil_form,
        'client_form': client_form,

    }
    return render(request, 'cases/civil-add.html', context)


def AjaxCivilClient(request):
    # 2IRIBe72eNUC381C41
    # request should be ajax and method should be GET.
    client_form = AdminClientCasesTypeForm()
    if request.method == "GET":
        # get the nick name from the client side.

        client_q = request.GET.get("client_name", None)
        print(client_q)

        if Client.objects.get(id=client_q):
            match_client = Client.objects.get(id=client_q)
            print('match_client', match_client)
            context = {
                'match_client': match_client,
                'client_form': client_form,
            }
            data = {'rendered_table': render_to_string('cases/ajaxclientget.html', context=context)}
            return JsonResponse(data, status=200)
        else:
            match_client = None
            messages.warning(request, "No user with this nuc")
            error_network = 'No user with this search'
            print('match_client', match_client)
            context = {
                'messages': 'No user with this nuc',
                'error_network': error_network,
                'client_form': client_form,
            }
            print('not found user')
        data = {'rendered_table': render_to_string('cases/ajaxclientget.html', context=context)}
        return JsonResponse(data, status=200)



def autocompleteModel(request):
    if request.is_ajax():
        q = request.GET.get('term', '').capitalize()
        search_qs = Client.objects.filter(client__startswith=q)
        results = []

        for r in search_qs:
            results.append(r.FIELD)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)