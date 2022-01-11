from django.contrib.auth import get_user_model
from django.db import models
# Create your models here.
from django.template.defaultfilters import slugify
from django.urls import reverse

from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from tinymce.models import HTMLField

from helper.modelHelper import STATUS, USER_STATUS

User = get_user_model()


class Categories(MPTTModel):
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    title_ar = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/category/%Y/%m/%d')
    status = models.CharField(max_length=20, choices=STATUS)
    slug = models.SlugField(null=True, blank=True, max_length=128, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        # ordering = ('title',)
        verbose_name = 'category'
        # verbose_name_plural = 'categories'

    class MPTTMeta:
        order_insertion_by = ['title']

    class TranslatableMeta:
        fields = ['title', ]

    def get_absolute_url(self):
        return reverse("category_list")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Categories, self).save(*args, **kwargs)


class Tags(models.Model):
    title = models.CharField(max_length=1500, null=False, blank=False)
    keyword = models.CharField(max_length=3500, null=False, blank=False)
    status = models.CharField(max_length=60, choices=STATUS, null=True, default='Inactive')
    slug = models.SlugField(unique=True, null=True, blank=True, max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('ServicesDetail', args=[str(self.id)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Tags, self).save(*args, **kwargs)


class Services(models.Model):
    title = models.CharField(max_length=1500, null=False, blank=False)
    keyword = models.CharField(max_length=3500, null=False, blank=False)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    is_featured = models.CharField(max_length=255, choices=STATUS, default='Inactive')
    long_desc = HTMLField()
    image = models.ImageField(blank=True, upload_to='images/Services/%Y/%m/%d')
    banner = models.ImageField(blank=True, upload_to='images/Services/%Y/%m/%d')
    banner_second = models.ImageField(blank=True, upload_to='images/Services/%Y/%m/%d')
    tags = models.ForeignKey(Tags, on_delete=models.CASCADE, blank=True, null=True)
    brand = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=60, choices=STATUS, null=True, default='Inactive')
    sort_order = models.SmallIntegerField(default=0, null=True)
    slug = models.SlugField(unique=True, null=True, blank=True, max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('ServicesDetail', args=[str(self.id)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Services, self).save(*args, **kwargs)


class OurWork(models.Model):
    title = models.CharField(max_length=1500, null=False, blank=False)
    keyword = models.CharField(max_length=3500, null=False, blank=False)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    is_featured = models.CharField(max_length=255, choices=STATUS, default='Inactive')
    long_desc = HTMLField()
    image = models.ImageField(blank=True, upload_to='images/Services/%Y/%m/%d')
    banner = models.ImageField(blank=True, upload_to='images/Services/%Y/%m/%d')
    banner_second = models.ImageField(blank=True, upload_to='images/Services/%Y/%m/%d')
    project_name = models.CharField(max_length=255, null=True, blank=True)
    project_type = models.CharField(max_length=255, null=True, blank=True)
    skills = models.CharField(max_length=255, null=True, blank=True)
    demo = models.URLField(max_length=255, null=True, blank=True)
    files = models.FileField(blank=True, upload_to='files/Services/%Y/%m/%d')
    pdf = models.FileField(blank=True, upload_to='files/Services/%Y/%m/%d')
    cloud_file = models.URLField(max_length=255, null=True, blank=True)
    tags = models.ForeignKey(Tags, on_delete=models.CASCADE, blank=True, null=True)
    brand = models.CharField(max_length=255, null=True, blank=True)

    status = models.CharField(max_length=60, choices=USER_STATUS, null=True, default='Inactive')
    sort_order = models.SmallIntegerField(default=0, null=True)
    slug = models.SlugField(unique=True, null=True, blank=True, max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('OurWorkDetail', args=[str(self.id)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(OurWork, self).save(*args, **kwargs)


class Products(models.Model):
    title = models.CharField(max_length=1500, null=False, blank=False)
    keyword = models.CharField(max_length=3500, null=False, blank=False)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    is_featured = models.CharField(max_length=255, choices=STATUS, default='Inactive')
    long_desc = HTMLField()
    project_name = models.CharField(max_length=255, null=True, blank=True)
    project_type = models.CharField(max_length=255, null=True, blank=True)
    skills = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(blank=True, upload_to='images/Services/%Y/%m/%d')
    files = models.FileField(blank=True, upload_to='files/Services/%Y/%m/%d')
    pdf = models.FileField(blank=True, upload_to='files/Services/%Y/%m/%d')
    demo = models.URLField(max_length=255, null=True, blank=True)
    cloud_file = models.URLField(max_length=255, null=True, blank=True)
    tags = models.ForeignKey(Tags, on_delete=models.CASCADE, blank=True, null=True)
    brand = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=60, choices=USER_STATUS, null=True, default='Inactive')
    sort_order = models.SmallIntegerField(default=0, null=True)
    slug = models.SlugField(unique=True, null=True, blank=True, max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('ProductDetail', args=[str(self.id)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Products, self).save(*args, **kwargs)


class Features(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=True)
    features_title = models.CharField(max_length=255, null=False, blank=False)
    features_keyword = models.CharField(max_length=800, null=False, blank=False)
    features_category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    features_name = models.CharField(max_length=255, null=True, blank=True)
    features_description = models.CharField(max_length=255, null=True, blank=True)
    icon = models.CharField(max_length=3500, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.features_name

    class Meta:
        ordering = ['id']


class ProductSkills(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=True)
    product_skill = models.CharField(max_length=1500, null=False, blank=False)
    percentage = models.CharField(max_length=150, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_skill

    class Meta:
        ordering = ['product_skill']


class Contact(models.Model):
    STATUS = (
        ('True', 'Enable'),
        ('False', 'Disable'),
    )
    name = models.CharField(max_length=50, null=False, )
    email = models.EmailField(max_length=50, null=False, )
    message = models.TextField(null=False, )
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
