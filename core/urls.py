from django.urls import path

from core.views.core import AdminIndex, CategoryList, CategoriesCreate, CategoriesDetail, CategoriesUpdate, \
    CategoriesDelete, TagsList, TagsCreate, TagsDetail, TagsUpdate, TagsDelete
from core.views.design import SliderView, SliderDetailView, SliderCreate, SliderEdit, SliderDelete, BannersView, \
    BannerCreate, BannerDetailView, BannerEdit, BannerDelete
from core.views.notifications import admin_notifications
from core.views.products import ProductList, ProductDetail, ProductUpdate, ProductDelete, ProductAdd
from core.views.services import ServicesList, ServicesCreate, ServicesDetail, ServicesUpdate, ServicesDelete
from core.views.setting import AdminSetting, AdminAddSetting, AdminSettingDetail
from core.views.users import AdminLogin, AdminLogout, AdminUsersList, AdminUserCreate, AdminLockscreen
from core.views.work import OurWorkList, OurWorkCreate, OurWorkDetail, OurWorkUpdate, OurWorkDelete
from core.views.localization import CountryListView, CountryCreate, CountryDetailView, CountryEdit, CountryDelete, \
    CurrencyListView, CurrencyCreate, CurrencyDetailView, CurrencyEdit, CurrencyDelete, LanguageListView, \
    LanguageCreate, LanguageEdit, LanguageDelete, GovernoratesListView, GovernoratesCreate, \
    GovernoratesDetailView, GovernoratesEdit, GovernoratesDelete, CityDelete, CityEdit, CityDetailView, CityCreate, \
    CityListView, AreaDelete, AreaEdit, AreaDetailView, AreaCreate, AreaListView
from core.reports.localization import country_export_data, country_import_data, governorates_export_data, \
    governorates_import_data, city_export_data, city_import_data, area_export_data, area_import_data
app_name = 'core'

urlpatterns = [

    path('', AdminIndex, name='AdminIndex'),
    path('login/', AdminLogin.as_view(), name='AdminLogin'),
    path('lockscreen', AdminLockscreen.as_view(), name='AdminLockscreen'),
    path('logout/', AdminLogout, name='AdminLogout'),

    path('dashboard/notifications/', admin_notifications, name='AdminNotifications'),

    ########## Category Admin #########
    path('category/', CategoryList.as_view(), name='AdminCategory'),
    path('category/add/', CategoriesCreate.as_view(), name='AdminAddCategory'),
    path('category/deatail/<int:pk>/', CategoriesDetail.as_view(), name='AdminDetailsCategory'),
    path('category/update/<int:pk>/', CategoriesUpdate.as_view(), name='AdminUpdateCategory'),
    path('category/delete/<int:pk>/', CategoriesDelete.as_view(), name='AdminDeleteCategory'),

    ########## Tags Admin #########
    path('tags/', TagsList.as_view(), name='AdminTags'),
    path('tags/add/', TagsCreate.as_view(), name='AdminAddTags'),
    path('tags/deatail/<int:pk>/', TagsDetail.as_view(), name='AdminDetailsTags'),
    path('tags/update/<int:pk>/', TagsUpdate.as_view(), name='AdminUpdateTags'),
    path('tags/delete/<int:pk>/', TagsDelete.as_view(), name='AdminDeleteTags'),

########## Services Admin #########
    path('services/', ServicesList.as_view(), name='AdminServices'),
    path('services/add/', ServicesCreate.as_view(), name='AdminAddServices'),
    path('services/deatail/<int:pk>/', ServicesDetail.as_view(), name='AdminDetailsServices'),
    path('services/update/<int:pk>/', ServicesUpdate.as_view(), name='AdminUpdateServices'),
    path('services/delete/<int:pk>/', ServicesDelete.as_view(), name='AdminDeleteServices'),

########## OurWork Admin #########
    path('work/', OurWorkList.as_view(), name='AdminOurWork'),
    path('work/add/', OurWorkCreate.as_view(), name='AdminAddOurWork'),
    path('work/deatail/<int:pk>/', OurWorkDetail.as_view(), name='AdminDetailsOurWork'),
    path('work/update/<int:pk>/', OurWorkUpdate.as_view(), name='AdminUpdateOurWork'),
    path('work/delete/<int:pk>/', OurWorkDelete.as_view(), name='AdminDeleteOurWork'),

    ########## Product Admin #########
    path('product/', ProductList.as_view(), name='AdminProduct'),
    path('product/add/', ProductAdd, name='AdminAddProduct'),

    path('product/deatail/<int:pk>/', ProductDetail.as_view(), name='AdminDetailsProduct'),
    path('product/update/<int:pk>/', ProductUpdate.as_view(), name='AdminUpdateProduct'),
    path('product/delete/<int:pk>/', ProductDelete.as_view(), name='AdminDeleteProduct'),


    ########## Users Admin #########
    path('user/', AdminUsersList.as_view(), name='AdminUser'),
    path('user/add/', AdminUserCreate.as_view(), name='AdminAddUser'),
    path('user/deatail/<int:pk>/', ServicesDetail.as_view(), name='AdminDetailsSUser'),
    path('user/update/<int:pk>/', ServicesUpdate.as_view(), name='AdminUpdateUser'),
    path('user/delete/<int:pk>/', ServicesDelete.as_view(), name='AdminDeleteUser'),

    ########## Site Setting Admin #########
    path('setting/', AdminSetting.as_view(), name='AdminSetting'),
    path('setting/add/', AdminAddSetting, name='AdminAddSetting'),
    path('setting/deatail/<int:pk>/', AdminSettingDetail.as_view(), name='AdminDetailsSetting'),
    path('setting/update/<int:pk>/', ServicesUpdate.as_view(), name='AdminUpdateSetting'),
    path('setting/delete/<int:pk>/', ServicesDelete.as_view(), name='AdminDeleteSetting'),


 ########## Slider   #########
    path('slider', SliderView.as_view(), name='AdminSlider'),
    path('slider/create/', SliderCreate.as_view(), name='AdminAddSlider'),
    path('slider/<int:pk>/', SliderDetailView.as_view(), name='AdminSliderDetail'),

path('slider/edit/<int:pk>/', SliderEdit.as_view(), name='AdminSliderEdit'),
    path('slider/delete/<int:pk>/', SliderDelete.as_view(), name='AdminSliderDelete'),

    ########## Banners   #########
    path('banner', BannersView.as_view(), name='AdminBanner'),
    path('banner/create/', BannerCreate, name='AdminAddBanner'),
    path('banner/<int:pk>/', BannerDetailView.as_view(), name='AdminBannerDetail'),
    path('banner/edit/<int:pk>/', BannerEdit.as_view(), name='AdminBannerEdit'),
    path('banner/delete/<int:pk>/', BannerDelete.as_view(), name='AdminBannerDelete'),
    ########## localization   #########
    path('lang', LanguageListView.as_view(), name='AdminLanguageListView'),
    path('lang/create/', LanguageCreate.as_view(), name='AdminLanguageCreate'),
    path('lang/update/<int:pk>/', LanguageEdit.as_view(), name='AdminLanguageEdit'),
    path('lang/delete/<int:pk>/', LanguageDelete.as_view(), name='AdminLanguageDelete'),

    path('country', CountryListView.as_view(), name='AdminCountryListView'),
    path('country/create/', CountryCreate.as_view(), name='AdminCountryCreate'),
    path('country/<int:pk>/', CountryDetailView.as_view(), name='AdminCountryDetailView'),
    path('country/update/<int:pk>/', CountryEdit.as_view(), name='AdminCountryEdit'),
    path('country/delete/<int:pk>/', CountryDelete.as_view(), name='AdminCountryDelete'),
    path('country/report/export/', country_export_data, name="AdminCountryReportExport"),
    path('country/report/import/', country_import_data, name="AdminCountryReportImport"),

    path('governorates', GovernoratesListView.as_view(), name='AdminGovernoratesListView'),
    path('governorates/create/', GovernoratesCreate.as_view(), name='AdminGovernoratesCreate'),
    path('governorates/<int:pk>/', GovernoratesDetailView.as_view(), name='AdminGovernoratesDetailView'),
    path('governorates/update/<int:pk>/', GovernoratesEdit.as_view(), name='AdminGovernoratesEdit'),
    path('governorates/delete/<int:pk>/', GovernoratesDelete.as_view(), name='AdminGovernoratesDelete'),
    path('governorates/report/export/', governorates_export_data, name="AdminGovernoratesReportExport"),
    path('governorates/report/imprt/', governorates_import_data, name="AdminGovernoratesReportImport"),

    path('city', CityListView.as_view(), name='AdminCityListView'),
    path('city/create/', CityCreate.as_view(), name='AdminCityCreate'),
    path('city/<int:pk>/', CityDetailView.as_view(), name='AdminCityDetailView'),
    path('city/update/<int:pk>/', CityEdit.as_view(), name='AdminCityEdit'),
    path('city/delete/<int:pk>/', CityDelete.as_view(), name='AdminCityDelete'),
    path('city/report/export/', city_export_data, name="AdminCityReportExport"),
    path('city/report/import/', city_import_data, name="AdminCityReportImport"),

    path('area', AreaListView.as_view(), name='AdminAreaListView'),
    path('area/create/', AreaCreate.as_view(), name='AdminAreaCreate'),
    path('area/<int:pk>/', AreaDetailView.as_view(), name='AdminAreaDetailView'),
    path('area/update/<int:pk>/', AreaEdit.as_view(), name='AdminAreaEdit'),
    path('area/delete/<int:pk>/', AreaDelete.as_view(), name='AdminAreaDelete'),
    path('area/report/export/', area_export_data, name="AdminAreaReportExport"),
    path('area/report/import/', area_import_data, name="AdminAreaReportImport"),

    path('currency', CurrencyListView.as_view(), name='AdminCurrencyListView'),
    path('currency/create/', CurrencyCreate.as_view(), name='AdminCurrencyCreate'),
    path('currency/<int:pk>/', CurrencyDetailView.as_view(), name='AdminCurrencyDetailView'),
    path('currency/update/<int:pk>/', CurrencyEdit.as_view(), name='AdminCurrencyEdit'),
    path('currency/delete/<int:pk>/', CurrencyDelete.as_view(), name='AdminCurrencyDelete'),

]
