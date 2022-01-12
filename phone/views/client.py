from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

##########################      Services Admin            ################################
from phone.forms.client import AdminClientForm, AdminIMEIForm
from phone.models import Client, IMEI


class ClientList(ListView):
    model = Client
    template_name = 'client/admin.html'

    # @method_decorator(superuser_only)
    # def dispatch(self, *args, **kwargs):
    #     return super(ServicesList, self).dispatch(*args, **kwargs)


class ClientDetail(DetailView):
    model = Client
    context_object_name = 'client'
    template_name = 'client/details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    # @method_decorator(superuser_only)
    # def dispatch(self, *args, **kwargs):
    #     return super(ServicesDetail, self).dispatch(*args, **kwargs)


class ClientCreate(CreateView):
    model = Client
    # fields = '__all__'
    form_class = AdminClientForm
    template_name = 'client/add.html'
    success_url = reverse_lazy('phone:AdminClient')

    # @method_decorator(superuser_only)
    # def dispatch(self, *args, **kwargs):
    #     return super(ServicesCreate, self).dispatch(*args, **kwargs)


class ClientUpdate(UpdateView):
    model = Client
    form_class = AdminClientForm
    template_name = 'client/update.html'
    success_url = reverse_lazy('core:AdminClient')

    # @method_decorator(superuser_only)
    # def dispatch(self, *args, **kwargs):
    #     return super(ServicesUpdate, self).dispatch(*args, **kwargs)


class ClientDelete(DeleteView):
    model = Client
    fields = '__all__'
    success_url = reverse_lazy('core:AdminClient')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    # @method_decorator(superuser_only)
    # def dispatch(self, *args, **kwargs):
    #     return super(ServicesDelete, self).dispatch(*args, **kwargs)


##########################      Services Admin            ################################
class IMEIList(ListView):
    model = IMEI
    template_name = 'imei/admin.html'

    # @method_decorator(superuser_only)
    # def dispatch(self, *args, **kwargs):
    #     return super(ServicesList, self).dispatch(*args, **kwargs)


class IMEIDetail(DetailView):
    model = IMEI
    context_object_name = 'imei'
    template_name = 'imei/details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    # @method_decorator(superuser_only)
    # def dispatch(self, *args, **kwargs):
    #     return super(ServicesDetail, self).dispatch(*args, **kwargs)


class IMEICreatee(CreateView):
    model = IMEI
    # fields = '__all__'
    form_class = AdminIMEIForm
    template_name = 'imei/add.html'
    success_url = reverse_lazy('core:AdminIMEI')

    # @method_decorator(superuser_only)
    # def dispatch(self, *args, **kwargs):
    #     return super(ServicesCreate, self).dispatch(*args, **kwargs)


@login_required(login_url='/dashboard/login')
# @superuser_only
def IMEICreate(request):  # sourcery skip: aug-assign, convert-to-enumerate
    client = Client.objects.all()

    if request.method == "POST":
        print(request)
        imei_form = AdminIMEIForm(request.POST or None, request.FILES or None)
        if imei_form.is_valid():
            print(request.POST)
            imei_form = True
            client = request.POST.get('client')
            imei_number = request.POST.get('imei_number')
            buy_date = request.POST.get('buy_date')
            imei_check = request.POST.get('imei_check')
            image = request.FILES.get('image')
            client_id = Client.objects.get(client=client)
            imei_form = None
            if not imei_form:
                print(request)
                print(request.POST)
                imei_form = IMEI(client=client_id, imei_number=imei_number, sell_date=buy_date,
                                 imei_check=imei_check, image=image)

                imei_form.save()

                messages.success(request,
                                 "Yeeew, check it out on the home page!")
                return HttpResponseRedirect(reverse_lazy('phone:AdminIMEI'))
            else:
                print("Form invalid, see below error msg")
                print(request.POST)
                messages.error(request, "Error")
    else:
        imei_form = AdminIMEIForm()

        context = {

            'client': client,
            'imei_form': imei_form,

        }
        return render(request, 'imei/add.html', context)
    context = {
        'client': client,
        'imei_form': imei_form,

    }
    return render(request, 'imei/add.html', context)


def AjaxIMEIClient(request):
    # 2IRIBe72eNUC381C41
    # request should be ajax and method should be GET.
    if request.method == "GET":
        # get the nick name from the client side.

        client_q = request.GET.get("client_name", None)
        print(client_q)

        if Client.objects.filter(client=client_q):
            match_client = Client.objects.get(client=client_q)
            print('match_client', match_client)
            context = {
                'match_client': match_client,
            }
            data = {'rendered_table': render_to_string('imei/ajaxclientget.html', context=context)}
            return JsonResponse(data, status=200)
        elif Client.objects.filter(client_code=client_q):
            match_client = Client.objects.get(client_code=client_q)
            print('match_client', match_client)
            context = {
                'match_client': match_client,
            }
            print('not found user')
            data = {'rendered_table': render_to_string('imei/ajaxclientget.html', context=context)}
            return JsonResponse(data, status=200)
        elif Client.objects.filter(national_id=client_q):
            match_client = Client.objects.get(national_id=client_q)
            print('match_client', match_client)
            context = {
                'match_client': match_client,
            }
            print('not found user')
            data = {'rendered_table': render_to_string('imei/ajaxclientget.html', context=context)}
            return JsonResponse(data, status=200)
        elif Client.objects.filter(phone=client_q):
            match_client = Client.objects.get(phone=client_q)
            print('match_client', match_client)
            context = {
                'match_client': match_client,
            }
            print('not found user')
            data = {'rendered_table': render_to_string('imei/ajaxclientget.html', context=context)}
            return JsonResponse(data, status=200)
        else:
            match_client = None
            messages.warning(request, "No user with this nuc")
            error_network = 'No user with this search'
            print('match_client', match_client)
            context = {
                'messages': 'No user with this nuc',
                'error_network': error_network,
            }
            print('not found user')
            data = {'rendered_table': render_to_string('imei/ajaxclientget.html', context=context)}
            return JsonResponse(data, status=200)

        return JsonResponse({}, status=400)


class IMEIUpdate(UpdateView):
    model = IMEI
    form_class = AdminIMEIForm
    template_name = 'imei/update.html'
    success_url = reverse_lazy('core:AdminIMEI')

    # @method_decorator(superuser_only)
    # def dispatch(self, *args, **kwargs):
    #     return super(ServicesUpdate, self).dispatch(*args, **kwargs)


class IMEIDelete(DeleteView):
    model = IMEI
    fields = '__all__'
    success_url = reverse_lazy('core:AdminIMEI')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    # @method_decorator(superuser_only)
    # def dispatch(self, *args, **kwargs):
    #     return super(ServicesDelete, self).dispatch(*args, **kwargs)
