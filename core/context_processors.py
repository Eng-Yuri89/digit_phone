from django.contrib.auth import get_user_model
from django.db.models import Sum

from blog.models import Article
from core.models.design import Setting
from core.models.services import Products

User = get_user_model()
def notifications(request):
    try:
        if not request.user.is_authenticated:
            return {
                'admin_notifications': None,


            }
        admin = User.objects.get(is_superuser=True)

        if request.user.is_authenticated and admin:
            return {'admin_notifications': request.user.notifications.filter(is_read=False, to_user=admin)}

    except Exception as e:
        if not request.user.is_authenticated:
            return {
                'admin_notifications': None,
                'seller_notifications': None,
                'deliver_notifications': None,

            }
        admin = User.objects.filter(is_superuser=True)

        if request.user.is_authenticated and admin:
            return {'admin_notifications': None}

def admin_summary(request):
    try:
        article_view = Article.objects.filter(status='Publish').aggregate(TOTAL=Sum('views'))['TOTAL']

        return {
                #'admin_earnings_total': Order.objects.filter(status='New').aggregate(total=sum('total')),
            #'admin_earnings_total': Order.objects.aggregate(total_price=Sum('total')),
            'admin_article_view': article_view,
            'admin_products_count': Products.objects.all().count(),
            'need_active': Setting.objects.filter(status=True),



        }
    except Exception as e:
        return {
            #'admin_earnings_total':  Order.objects.aggregate(total=Sum('total')),
            'admin_products_count': Products.objects.all().count(),
            'need_active': Setting.objects.filter(status=True),
            'new_vendor': Setting.objects.filter(status=True),
                }

# def admin_chart(request):
#     try:
#         order = Order.objects.values('address', 'total', 'payment_method')
#         print(order)
#         data = {
#             'data': [
#                 {
#                     'address': item['address'],
#                     'total': float(item['total']),
#                     'payment_method': item['payment_method'],
#                 }
#                 for item in order
#             ]
#         }
#
#         return {
#
#             'admin_orders_location': data,
#
#         }
#     except Exception as e:
#         return {
#
#             'admin_orders_location': None,
#
#                 }