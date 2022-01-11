from django.core.paginator import Paginator, PageNotAnInteger
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import ListView, DetailView

from blog.models import Article, Category, Tag


def test(request):
    return render(request, 'front/product/product-details.html', )


##########################      Services Admin            ################################


def BlogList(request):
    articles = Article.objects.all()

    all_category = Category.objects.all()

    all_tag = Tag.objects.all()


    context = {'articles': articles,
               'all_category': all_category,
               'all_tag': all_tag,}
    return render(request, 'front/blog/blog.html', context)

def ArticleDetailFront(request,slug):
    articles = Article.objects.all()
    article = Article.objects.get(slug=slug)
    all_category = Category.objects.all()
    article_category = Category.objects.get(article=article)
    all_tag = Tag.objects.all()
    article_tag = Tag.objects.filter(article=article)
    article.viewed()
    context = {'articles': articles,'article': article,
               'all_category': all_category,'article_category': article_category,
               'all_tag': all_tag,'article_tag': article_tag,}
    return render(request, 'front/blog/article-detail.html', context)



class ArticleCategoryList(ListView):
    model = Category
    template_name = 'front/blog/blog.html'


class ArticleCategoryDetailFront(DetailView):
    model = Category

    template_name = 'front/blog/article-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class ArticleTagList(ListView):
    model = Tag
    template_name = 'front/blog/blog.html'


class ArticleTagDetailFront(DetailView):
    model = Tag

    template_name = 'front/blog/article-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


def ProductSearch(request):
    q = request.GET['q']
    data = Article.objects.filter(title__icontains=q).order_by('-id')
    images = Article.objects.filter(article__title=q, )
    context = {'data': data,
               'images': images,
               }
    return render(request, 'Search/search_products.html', context)
