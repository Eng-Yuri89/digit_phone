from django.urls import path

from .views.firebase import login_firebase, firebase_login_save
from .views.user import UserSignup, UserActivate, UserLogin, UserLogout, \
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, \
    TestPages

app_name = 'user'

urlpatterns = [

    # path('guest-user/', guest_user_view, name='guest_user_register'),

    ##########User################
    path('signup/', UserSignup, name='CustomerRegister'),
    path('activate/<uidb64>/<token>/', UserActivate, name='activate'),
    path('login/', UserLogin.as_view(), name='CustomerLogin'),
    path('logout/', UserLogout, name='CustomerLogout'),
    path('test/', TestPages, name='TestPages'),

    ###########Password###########
    path('reset_password/', PasswordResetView.as_view(), name="ResetPassword"),
    path('reset_password_sent/', PasswordResetDoneView.as_view(), name="passwordResetDone"),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name="passwordResetConfirm"),
    path('reset_password_complete/', PasswordResetCompleteView.as_view(), name="passwordResetComplete"),


########## Firebase Login  Front #########
    path("login_firebase", login_firebase,name='LoginFireBase'),
    path("firebase_login_save", firebase_login_save,name='firebase_login_save'),

]
