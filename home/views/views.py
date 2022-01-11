import logging

from django.shortcuts import render
# Create your views here.
from django.views.generic import ListView, DetailView

from core.models.services import Tags, Categories


def HomeIndex(request):
    return render(request, 'frontend/index.html', )


class TagsList(ListView):
    model = Tags
    template_name = 'catalog/tags/admin.html'

    # @method_decorator(superuser_only)
    # def dispatch(self, *args, **kwargs):
    #     return super(TagsList, self).dispatch(*args, **kwargs)


class TagsDetail(DetailView):
    model = Categories
    context_object_name = 'tags'
    template_name = 'catalog/tags/details.html'


logger = logging.getLogger(__name__)


def page_not_found_view(
        request,
        exception,
        template_name='blog/error_page.html'):
    if exception:
        logger.error(exception)
    url = request.get_full_path()
    return render(request,
                  template_name,
                  {'message': '哎呀，您访问的地址 ' + url + ' 是一个未知的地方。请点击首页看看别的？',
                   'statuscode': '404'},
                  status=404)


def server_error_view(request, template_name='blog/error_page.html'):
    return render(request,
                  template_name,
                  {'message': '哎呀，出错了，我已经收集到了错误信息，之后会抓紧抢修，请点击首页看看别的？',
                   'statuscode': '500'},
                  status=500)


def permission_denied_view(
        request,
        exception,
        template_name='blog/error_page.html'):
    if exception:
        logger.error(exception)
    return render(
        request, template_name, {
            'message': '哎呀，您没有权限访问此页面，请点击首页看看别的？', 'statuscode': '403'}, status=403)
