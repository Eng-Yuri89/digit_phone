"""digit_phone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.template.defaulttags import url
from django.urls import path, include, re_path



handler404 = 'home.views.views.page_not_found_view'
handler500 = 'home.views.views.server_error_view'
handle403 = 'home.views.views.permission_denied_view'
urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),

]
urlpatterns += i18n_patterns(
    path('', include('user.urls'), name='user'),
    path('dashboard/', include('core.urls'), name='core'),
    # path('admin/', admin.site.urls),
    path('', include('home.urls'), name='home'),
    path('', include('blog.urls'), name='blog'),
    path('', include('phone.urls'), name='phone'),


    path('tinymce/', include('tinymce.urls')),
    path('api-auth/', include('rest_framework.urls')),

    # path('^inbox/notifications/', include(notifications.urls, namespace='notifications')),
    prefix_default_language=False
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
