def AjaxAttorneyClient(request):
    # 2IRIBe72eNUC381C41
    # request should be ajax and method should be GET.
    if request.method == "GET":
        # get the nick name from the client side.

        client_q = request.GET.get("client_name", None)
        print(client_q)

        if Client.objects.filter(client=client_q):
            match_client = Client.objects.get(client=client_q)
        elif Client.objects.filter(client_code=client_q):
            match_client = Client.objects.get(client_code=client_q)
        elif Client.objects.filter(national_id=client_q):
            match_client = Client.objects.get(national_id=client_q)
        elif Client.objects.filter(phone=client_q):
            match_client = Client.objects.get(phone=client_q)
        else :
            match_client = None

        if Client.objects.filter(client=client_name) :
            match_user = Client.objects.get(client=client_name)
            print('match_user',match_user)
            try:
                network_user = Attorney.objects.get(client=match_user)
                network_full = 'The User Has Full Network Please Add Indirect Parent'
                context = {
                    'match_user': match_user,
                    'network_user': network_user,
                    'network_full': network_full,

                }
                print('1')
                messages.success(request, "The User Have Full Tree")

                data = {'rendered_table': render_to_string('imei/ajaxclientget.html', context=context)}
                return JsonResponse(data, status=200)
            except :
                pass

            print('2')

            # if nick_name found return not valid new friend
            context = {
                'match_user': match_user,
            }
            data = {'rendered_table': render_to_string('imei/ajaxclientget.html', context=context)}
            return JsonResponse(data, status=200)
            # return JsonResponse({"valid": True}, status=200)
        # elif User.objects.filter(nuc=direct_nuc).exists() or NetworkUser.objects.filter(direct_nuc=direct_nuc,
        #                                                                                 children_right__isnull=True) or NetworkUser.objects.filter(
        #         direct_nuc=direct_nuc, children_left__isnull=True):
        #
        #     match_user = User.objects.get(nuc=direct_nuc)
        #     try:
        #         network_user = NetworkUser.objects.get(root=match_user)
        #         network_ok = 'The User good to add  Network '
        #         context = {
        #             'match_user': match_user,
        #             'network_user': network_user,
        #             'network_ok': network_ok,
        #         }
        #         print('1')
        #         data = {'rendered_table': render_to_string('genealogy/genealogy/ajaxnucget.html', context=context)}
        #         return JsonResponse(data, status=200)
        #     except:
        #         messages.warning(request, "No Network with this nuc")
        #         error_network = 'No user with this nuc'
        #         print('eror fd')
        #         context = {
        #             'messages': 'No Network with this nuc',
        #             'error_network': error_network,
        #         }
        #         print('not found user')
        #         data = {'rendered_table': render_to_string('genealogy/genealogy/ajaxnucget.html', context=context)}
        #         return JsonResponse(data, status=200)


        else:
            # if nick_name not found, then user can create a new friend.
            messages.warning(request, "No user with this nuc")
            error_network = 'No user with this nuc'
            print('eror fd')
            context = {
                'messages': 'No user with this nuc',
                'error_network': error_network,
            }
            print('not found user')
            data = {'rendered_table': render_to_string('imei/ajaxclientget.html', context=context)}
            return JsonResponse(data, status=200)

    return JsonResponse({}, status=400)



def AjaxAttorneyClient(request):
    # 2IRIBe72eNUC381C41
    # request should be ajax and method should be GET.
    if request.method == "GET":
        # get the nick name from the client side.

        client_q = request.GET.get("client_name", None)
        print(client_q)

        if Client.objects.filter(client__in=client_q):
            match_client = Client.objects.get(client__in=client_q)
            print('match_client', match_client)
        elif Client.objects.filter(client_code__in=client_q):
            match_client = Client.objects.get(client_code__in=client_q)
            print('match_client', match_client)
        elif Client.objects.filter(national_id__in=client_q):
            match_client = Client.objects.get(national_id__in=client_q)
            print('match_client', match_client)
        elif Client.objects.filter(phone__in=client_q):
            match_client = Client.objects.get(phone__in=client_q)
            print('match_client', match_client)
        else :
            match_client = None
            messages.warning(request, "No user with this nuc")
            error_network = 'No user with this nuc'
            print('match_client',match_client)
            context = {
                'messages': 'No user with this nuc',
                'error_network': error_network,
            }
            print('not found user')
            data = {'rendered_table': render_to_string('imei/ajaxclientget.html', context=context)}
            return JsonResponse(data, status=200)

        return JsonResponse({}, status=400)

    results = Client.objects.annotate(
        search=SearchVector('client', 'client_code', 'national_id', 'phone'),
    ).filter(search=client_q)