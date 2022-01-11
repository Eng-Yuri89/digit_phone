from django.urls import path

from .views import AdminArticleList, ArticleCreate, ArticleDetail, ArticleUpdate, ArticleDelete, AdminTagList, \
    TagDelete, TagUpdate, TagDetail, TagCreate, CategoryDelete, CategoryUpdate, CategoryDetail, CategoryCreate, \
    AdminCategoryList

app_name = "blog"
urlpatterns = [

    ########## Blog Setting Admin #########
    path('dashboard/blog/', AdminArticleList.as_view(), name='AdminArticle'),
    path('dashboard/blog/add/', ArticleCreate.as_view(), name='AdminAddArticle'),
    path('dashboard/blog/deatail/<int:pk>/', ArticleDetail.as_view(), name='AdminDetailsArticle'),
    path('dashboard/blog/update/<int:pk>/', ArticleUpdate.as_view(), name='AdminUpdateArticle'),
    path('dashboard/blog/delete/<int:pk>/', ArticleDelete.as_view(), name='AdminDeleteArticle'),

    ########## Category Setting Admin #########
    path('dashboard/acategory/', AdminCategoryList.as_view(), name='AdminCategory'),
    path('dashboard/acategory/add/', CategoryCreate.as_view(), name='AdminAddCategory'),
    path('dashboard/acategory/deatail/<int:pk>/', CategoryDetail.as_view(), name='AdminDetailsCategory'),
    path('dashboard/acategory/update/<int:pk>/', CategoryUpdate.as_view(), name='AdminUpdateCategory'),
    path('dashboard/acategory/delete/<int:pk>/', CategoryDelete.as_view(), name='AdminDeleteCategory'),

    ########## Tag Setting Admin #########
    path('dashboard/tag/', AdminTagList.as_view(), name='AdminTag'),
    path('dashboard/tag/add/', TagCreate.as_view(), name='AdminAddTag'),
    path('dashboard/tag/deatail/<int:pk>/', TagDetail.as_view(), name='AdminDetailsTag'),
    path('dashboard/tag/update/<int:pk>/', TagUpdate.as_view(), name='AdminUpdateTag'),
    path('dashboard/tag/delete/<int:pk>/', TagDelete.as_view(), name='AdminDeleteTag'),

]
