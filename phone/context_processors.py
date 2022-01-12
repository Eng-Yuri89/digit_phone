from blog.models import Article, Category, Tag
from core.models.design import Setting
from core.models.services import Tags, Services, OurWork, Categories, Products
from lawyer.models.cases import CasesType


def lawyer_processors(request):
    try:
        return {
            'all_cases_type': CasesType.objects.all(),


        }
    except Exception as e:
        return {
            'all_cases_type': None,


        }
