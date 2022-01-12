# Create your views here.
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse_lazy

from phone.forms.client import AdminIMEIForm
from phone.models import Client, IMEI


def AddIMEIFrontss(request):
    return render(request, 'front/imei/add-imei.html', )


@login_required(login_url='/login')
def AddIMEIFront(request):  # sourcery skip: aug-assign, convert-to-enumerate
    client = Client.objects.all()

    if request.method == "POST":
        print(request)
        imei_form = AdminIMEIForm(request.POST or None, request.FILES or None)
        if imei_form.is_valid():
            print(request.POST)
            imei_form = True
            client = request.user.id
            imei_number = request.POST.get('imei_number')
            buy_date = request.POST.get('buy_date')
            imei_check = request.POST.get('imei_check')
            image = request.FILES.get('image')
            client_id = Client.objects.get(id=client)
            print(client_id)
            imei_form = None
            if not imei_form:
                print(request)
                print(request.POST)
                imei_form = IMEI(client=client_id, imei_number=imei_number, sell_date=buy_date,
                                 imei_check=imei_check, image=image)

                imei_form.save()

                messages.success(request,
                                 "Yeeew, check it out on the home page!")
                return HttpResponseRedirect(reverse_lazy('home:SuccessIMEIFront'))
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
        return render(request, 'front/imei/add-imei.html', context)
    context = {
        'client': client,
        'imei_form': imei_form,

    }
    return render(request, 'front/imei/add-imei.html', context)


def CheckIMEIFront(request):
    return render(request, 'front/imei/check-imei.html', )


def ImeiSuccess(request):
    return render(request, 'front/imei/imei-success.html', )


def AjaxIMEIClientFront(request):
    # 2IRIBe72eNUC381C41
    # request should be ajax and method should be GET.
    if request.method == "GET":
        # get the nick name from the client side.

        imei_q = request.GET.get("imei_q", None)
        print(imei_q)
    try:

        if IMEI.objects.filter(imei_number=imei_q):
            match_imei = IMEI.objects.get(imei_number=imei_q)
            print('match_imei', match_imei)
            context = {
                'match_imei': match_imei,
            }
            data = {'rendered_table': render_to_string('front/imei/ajaxclientfront.html', context=context)}
            return JsonResponse(data, status=200)
        else:
            match_imei = ' لايوجد رقم مطابق للرقم الذي ادخلته تاكد من الرقم او قم باضافته '
            messages.warning(request, "No user with this nuc")
            error_network = 'لايوجد رقم مطابق  تاكد من الرقم او قم باضافته'
            print('match_imei', match_imei)
            context = {
                'messages': 'No user with this nuc',
                'match_imei': match_imei,
                'error_network': error_network,
            }
            print('not found user')
            data = {'rendered_table': render_to_string('front/imei/ajaxclientfront.html', context=context)}
            return JsonResponse(data, status=200)
    except Exception as e:
        print('not found user', e)
        match_imei = ' قم باضافة ارقام فقط وليس أحرف '
        messages.warning(request, "No user with this nuc")
        error_network = 'قم باضافة ارقام فقط وليس أحرف '
        print('match_imei', match_imei)
        context = {
            'messages': 'No user with this nuc',
            'match_imei': match_imei,
            'error_network': error_network,
        }
        print('not found user')
        data = {'rendered_table': render_to_string('front/imei/ajaxclientfront.html', context=context)}
        return JsonResponse(data, status=200)

    return JsonResponse({}, status=400)
