import json
from django.contrib.auth import get_user_model, login
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from requests import request

from digit_phone import settings

User = get_user_model()


def login_firebase(request):
    return render(request, "users/dashboard/firebbase-login.html")


@csrf_exempt
def firebase_login_save(request):
    username = request.POST.get("username")
    email = request.POST.get("email")
    provider = request.POST.get("provider")
    token = request.POST.get("token")
    password = request.POST.get("password")
    print('token',token)
    print(username, email, provider, token)
    firebase_response = loadDatafromFirebaseApi(token)
    firebase_dict = json.loads(firebase_response)
    print('1',firebase_dict)
    if "users" in firebase_dict:
        user = firebase_dict["users"]
        if len(user) > 0:
            user_one = user[0]
            if "phoneNumber" in user_one:
                if user_one["phoneNumber"] == email:
                    data = proceedToLogin(request, email, username, token, provider)
                    return HttpResponse(data)
                else:
                    return HttpResponse("Invalid phone  Login Request")
            else:
                if email == user_one["email"]:
                    provider1 = user_one["providerUserInfo"][0]["providerId"]
                    if user_one["emailVerified"] == 1 or user_one["emailVerified"] == True or user_one[
                        "emailVerified"] == "True" or provider1 == "facebook.com":
                        data = proceedToLogin(request, email, username, token, provider)
                        return HttpResponse(data)
                    else:
                        return HttpResponse("Please Verify Your Email to Get Login")
                else:
                    return HttpResponse("Unknown Email User")
        else:
            return HttpResponse("Invalid Request User Not Found")
    else:
        return HttpResponse("Bad Request")


def loadDatafromFirebaseApi(token):
    url = "https://identitytoolkit.googleapis.com/v1/accounts:lookup"

    payload = 'key=AIzaSyD8deb1rqhHt45CKtPukgtvA_KWyJx-3ww&idToken=' + token

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = request("POST", url, headers=headers, data=payload)

    return response.text


def proceedToLogin(request, email, username, token, provider,):
    users = User.objects.filter(email=email).exists()

    if users == True:
        user_one = User.objects.get(email=email)
        user_one.backend = settings.AUTH_USER_MODEL
        login(request, user_one)
        return "login_success"
    else:
        user = User.objects.create_user(username=username, email=email, password='password')
        user_one = User.objects.get(email=email)
        user_one.backend = settings.AUTH_USER_MODEL
        login(request, user_one)
        return "login_success"
