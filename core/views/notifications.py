from django.contrib.auth import get_user_model
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from core.models.notifications import Notification

User = get_user_model()


@login_required
def admin_notifications(request):
    if request.user.is_authenticated and request.user.is_superuser:
        goto = request.GET.get('goto', '')
        notification_id = request.GET.get('notification', 0)
        extra_id = request.GET.get('extra_id', 0)
        notification_list = Notification.objects.filter(is_read=False)
        page = request.GET.get('page', 1)

        paginator = Paginator(notification_list, 10)
        try:
            notifications = paginator.page(page)
        except PageNotAnInteger:
            notifications = paginator.page(1)
        except EmptyPage:
            notifications = paginator.page(paginator.num_pages)

        if goto != '':
            notification = Notification.objects.get(pk=notification_id)
            notification.is_read = True
            notification.save()
            if notification.notification_type in [
                Notification.MESSAGE,
                Notification.APPLICATION,
                Notification.NewOrder,
                Notification.NewRegistration,
                Notification.NewVendorCreate,
            ]:
                return redirect('view_application', application_id=notification.extra_id)
        return render(request, 'notification/admin_notifications.html', {'notifications': notifications})


@login_required
def vendor_notifications(request):
    if request.user.is_authenticated and request.user.seller:
        goto = request.GET.get('goto', '')
        notification_id = request.GET.get('notification', 0)
        extra_id = request.GET.get('extra_id', 0)
        notification_list = Notification.objects.filter(is_read=False)
        page = request.GET.get('page', 1)

        paginator = Paginator(notification_list, 10)
        try:
            notifications = paginator.page(page)
        except PageNotAnInteger:
            notifications = paginator.page(1)
        except EmptyPage:
            notifications = paginator.page(paginator.num_pages)

        if goto != '':
            notification = Notification.objects.get(pk=notification_id)
            notification.is_read = True
            notification.save()
            if notification.notification_type in [
                Notification.MESSAGE,
                Notification.APPLICATION,
                Notification.NewOrder,
                Notification.NewRegistration,
                Notification.NewVendorCreate,
            ]:
                return redirect('view_application', application_id=notification.extra_id)
        return render(request, 'notification/vendor_notifications.html', {'notifications': notifications})

@login_required
def shipping_notifications(request):
    if request.user.is_authenticated and request.user.deliver:
        goto = request.GET.get('goto', '')
        notification_id = request.GET.get('notification', 0)
        extra_id = request.GET.get('extra_id', 0)
        notification_list = Notification.objects.filter(is_read=False)
        page = request.GET.get('page', 1)

        paginator = Paginator(notification_list, 10)
        try:
            notifications = paginator.page(page)
        except PageNotAnInteger:
            notifications = paginator.page(1)
        except EmptyPage:
            notifications = paginator.page(paginator.num_pages)

        if goto != '':
            notification = Notification.objects.get(pk=notification_id)
            notification.is_read = True
            notification.save()
            if notification.notification_type in [
                Notification.MESSAGE,
                Notification.APPLICATION,
                Notification.NewOrder,
                Notification.NewRegistration,
                Notification.NewVendorCreate,
            ]:
                return redirect('view_application', application_id=notification.extra_id)
        return render(request, 'notification/shipping_notifications.html', {'notifications': notifications})
