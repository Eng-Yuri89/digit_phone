from django.urls import path, re_path

from phone.views.client import ClientList, ClientCreate, ClientDetail, ClientUpdate, ClientDelete, IMEIList, IMEICreate, \
    IMEIDetail, IMEIUpdate, IMEIDelete, AjaxIMEIClient

app_name = 'phone'




urlpatterns = [

    ########## Client Admin #########
    path('dashboard/client/', ClientList.as_view(), name='AdminClient'),
    path('dashboard/client/add/', ClientCreate.as_view(), name='AdminAddClient'),
    path('dashboard/client/deatail/<int:pk>/', ClientDetail.as_view(), name='AdminDetailsClient'),
    path('dashboard/client/update/<int:pk>/', ClientUpdate.as_view(), name='AdminUpdateClient'),
    path('dashboard/client/delete/<int:pk>/', ClientDelete.as_view(), name='AdminDeleteClient'),

    ########## IMEI Admin #########
    path('dashboard/imei/', IMEIList.as_view(), name='AdminIMEI'),
    path('dashboard/imei/add/', IMEICreate, name='AdminAddIMEI'),
    path('dashboard/imei/deatail/<int:pk>/', IMEIDetail.as_view(), name='AdminDetailsIMEI'),
    path('dashboard/imei/update/<int:pk>/', IMEIUpdate.as_view(), name='AdminUpdateIMEI'),
    path('dashboard/imei/delete/<int:pk>/', IMEIDelete.as_view(), name='AdminDeleteIMEI'),
    path('dashboard/imei/client/', AjaxIMEIClient, name='AjaxIMEIClient'),

    # ########## Court Admin #########
    # path('dashboard/court/', CourtList.as_view(), name='AdminCourt'),
    # path('dashboard/court/add/', CourtCreate.as_view(), name='AdminAddCourt'),
    # path('dashboard/court/deatail/<int:pk>/', CourtDetail.as_view(), name='AdminDetailsCourt'),
    # path('dashboard/court/update/<int:pk>/', CourtUpdate.as_view(), name='AdminUpdateCourt'),
    # path('dashboard/court/delete/<int:pk>/', CourtDelete.as_view(), name='AdminDeleteCourt'),
    # path('dashboard/court/client/', AjaxAttorneyClient, name='AjaxAttorneyCourt'),
    #
    # ########## Court Circuit Admin #########
    # path('dashboard/circuit/', CourtCircuitList.as_view(), name='AdminCourtCircuit'),
    # path('dashboard/circuit/add/', CourtCircuitCreate.as_view(), name='AdminAddCourtCircuit'),
    # path('dashboard/circuit/deatail/<int:pk>/', CourtCircuitDetail.as_view(), name='AdminDetailsCourtCircuit'),
    # path('dashboard/circuit/update/<int:pk>/', CourtCircuitUpdate.as_view(), name='AdminUpdateCourtCircuit'),
    # path('dashboard/circuit/delete/<int:pk>/', CourtCircuitDelete.as_view(), name='AdminDeleteCourtCircuit'),
    # path('dashboard/circuit/client/', AjaxAttorneyClient, name='AjaxAttorneyClient'),
    #
    # ########## Court Circuit Admin #########
    # path('dashboard/circuit/', CourtCircuitList.as_view(), name='AdminCourtCircuit'),
    # path('dashboard/circuit/add/', CourtCircuitCreate.as_view(), name='AdminAddCourtCircuit'),
    # path('dashboard/circuit/deatail/<int:pk>/', CourtCircuitDetail.as_view(), name='AdminDetailsCourtCircuit'),
    # path('dashboard/circuit/update/<int:pk>/', CourtCircuitUpdate.as_view(), name='AdminUpdateCourtCircuit'),
    # path('dashboard/circuit/delete/<int:pk>/', CourtCircuitDelete.as_view(), name='AdminDeleteCourtCircuit'),
    # path('dashboard/circuit/client/', AjaxAttorneyClient, name='AjaxAttorneyClient'),
    #
    # ########## Case Type  Admin #########
    # path('dashboard/cases/type/', CasesTypeList.as_view(), name='AdminCasesType'),
    # path('dashboard/cases/type/add/', CasesTypeCreate.as_view(), name='AdminAddCasesType'),
    # path('dashboard/cases/type/case/<slug:slug>/', CasesTypeDetail.as_view(), name='AdminDetailsCasesType'),
    # path('dashboard/cases/type/update/<int:pk>/', CasesTypeUpdate.as_view(), name='AdminUpdateCasesType'),
    # path('dashboard/cases/type/delete/<int:pk>/', CasesTypeDelete.as_view(), name='AdminDeleteCasesType'),




]
