import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.crypto import get_random_string
from django.utils.text import slugify

from helper.modelHelper import Civil_TYPE, IMEI_CHECK, CLIENT_TYPE

User = get_user_model()



class Client(models.Model):
    client = models.CharField(max_length=600, blank=False, null=False)
    client_code = models.CharField(unique=True, max_length=200, )
    address = models.CharField(max_length=600, blank=True, null=True)
    client_type = models.CharField(max_length=200, blank=False, null=False, choices=CLIENT_TYPE, )
    national_id = models.CharField(unique=True, max_length=200,blank=True, null=True )
    image = models.ImageField(upload_to='images/client/%y/%m', blank=True, null=True)
    phone = models.CharField(unique=True, max_length=200, )
    status = models.BooleanField(default=True,blank=True,null=True)
    slug = models.SlugField(null=True, blank=True, max_length=128, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        # ordering = ('title',)
        verbose_name = 'lawyer_client'
        # verbose_name_plural = 'categories'

    class MPTTMeta:
        order_insertion_by = ['client']

    def __str__(self):
        return f"{self.client}"

    def save(self, *args, **kwargs):
        if not self.client_code and not self.slug:
            self.client_code =  'CLI' + get_random_string(5).upper()
            self.slug = slugify(self.client)
        super(Client, self).save(*args, **kwargs)


class IMEI(models.Model):
    client = models.ForeignKey(Client, related_name='client_imei', on_delete=models.PROTECT)
    imei_number = models.PositiveIntegerField(blank=False, null=False,unique=True)
    imei_code = models.CharField(unique=True, max_length=200, )
    buy_date = models.DateField(blank=True, null=True)
    sell_date = models.DateField(blank=True, null=True)
    imei_check = models.CharField(max_length=200, blank=False, null=False,choices=IMEI_CHECK,)
    image = models.ImageField(upload_to='images/IMEI/%y/%m', blank=True, null=True)
    status = models.BooleanField(default=True)
    slug = models.SlugField(null=True, blank=True, max_length=128, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        # ordering = ('title',)
        verbose_name = 'imei_user'
        # verbose_name_plural = 'categories'

    class MPTTMeta:
        order_insertion_by = ['imei_number']

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        if not self.imei_code and not self.slug:
            self.imei_code = 'IMEI-' + get_random_string(5).upper()
            self.slug = slugify(self.imei_code)
        super(IMEI, self).save(*args, **kwargs)