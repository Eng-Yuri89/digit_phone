from django.urls import path

from home.views.blog import BlogList, ArticleDetailFront, ArticleTagDetailFront, ArticleCategoryDetailFront
from home.views.contact import  contact_view
from home.views.product import ProductDetail
from home.views.services import ServicesList, ServicesDetail
from home.views.views import HomeIndex

app_name = 'home'

urlpatterns = [

    path('', HomeIndex, name='HomeIndex'),
    path("contact", contact_view, name="Contact"),

    ########## Services Front #########
    path('services/', ServicesList.as_view(), name='AllServices'),

    path('services/<slug:slug>/', ServicesDetail.as_view(), name='FrontDetailsServices'),

    path('product/<slug:slug>', ProductDetail.as_view(), name='FrontDetailsProduct'),

    ########## Blog Front #########
    path('blog/', BlogList, name='Blog'),
    path('blog/<slug:slug>', ArticleDetailFront, name='FrontArticleDetails'),
    path('blog/category/<slug:slug>', ArticleCategoryDetailFront.as_view(), name='FrontArticleCategoryDetails'),
    path('blog/tag/<slug:slug>', ArticleTagDetailFront.as_view(), name='FrontArticleTagDetails'),

    # path('admin/logout', AdminIndex, name='AdminIndex'),

]
