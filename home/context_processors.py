from blog.models import Article, Category, Tag
from core.models.design import Setting
from core.models.services import Tags, Services, OurWork, Categories, Products


def home_processors(request):
    try:
        return {
            'all_category': Categories.objects.all(),
            'all_tags': Tags.objects.all(),
            'all_work': OurWork.objects.all(),
            'all_services': Services.objects.all(),
            'all_product': Products.objects.all(),
            'all_setting': Setting.objects.get(status='Active', slug='diithuptt'),
            'all_article': Article.objects.all(),
            'category_article': Category.objects.all(),
            'tag_article': Tag.objects.all(),

        }
    except Exception as e:
        return {
            'all_category': None,
            'all_tags': None,
            'all_work': None,
            'all_services': None,
            'all_product': None,
            'all_setting': None,
            'all_article': None,
            'category_article': None,
            'tag_article': None,

        }
