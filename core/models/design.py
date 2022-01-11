# Create your models here.
from django.db import models
# Create your models here.
from django.template.defaultfilters import slugify

from mptt.models import MPTTModel
from tinymce.models import HTMLField

from core.models.localization import Country
from core.models.services import Categories
from helper.modelHelper import STATUS


class Setting(models.Model):
    title = models.CharField(max_length=150, null=True, default='Digithup')
    keywords = models.CharField(max_length=255, default=' ', null=True)
    copyright = models.CharField(max_length=50, default=' ', null=True)
    email = models.EmailField(blank=True, max_length=50, default='', null=True)
    image = models.ImageField(upload_to='images/setting/%Y/%m/%d', default='images/Ydoob.png')
    facebook = models.URLField(blank=True, max_length=50, default='', null=True)
    instagram = models.URLField(blank=True, max_length=50, default='', null=True)
    twitter = models.URLField(blank=True, max_length=50, default='', null=True)
    linkedin = models.URLField(blank=True, max_length=50, default='', null=True)
    behance = models.URLField(blank=True, max_length=50, default='', null=True)
    youtube = models.URLField(blank=True, max_length=50, default='', null=True)
    status = models.CharField(max_length=10, choices=STATUS, default='Inactive', unique=True)
    slug = models.SlugField(unique=True)
    create_at = models.DateTimeField(auto_now=True, null=False)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)




class ExtraSetting(models.Model):
    setting = models.ForeignKey(Setting, on_delete=models.CASCADE)  #
    phone = models.IntegerField(blank=True, default='510')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)
    address = models.CharField(blank=True, max_length=100, null=True)
    about = HTMLField(blank=True, default='', null=True)
    contact = HTMLField(blank=True, default='', null=True)
    extra_keywords = models.CharField(max_length=255, blank=True, null=True)


class SeoSetting(models.Model):
    setting = models.ForeignKey(Setting, on_delete=models.CASCADE)  #
    seo_description = models.CharField(max_length=600, verbose_name='Meta Tag description')
    seo_author = models.CharField(max_length=255, verbose_name='Meta Tag author')
    seo_keywords = models.CharField(max_length=255)
    seo_title = models.CharField(max_length=255)
    seo_image = models.ImageField(upload_to='images/setting/%Y/%m/%d')
    seo_site_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


class SettingFeatures(models.Model):
    setting = models.ForeignKey(Setting, on_delete=models.CASCADE, null=True)
    features_title = models.CharField(max_length=255, null=False, blank=False)
    features_keyword = models.CharField(max_length=800, null=False, blank=False)
    icon =models.CharField(max_length=255, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.features_title

    class Meta:
        ordering = ['id']


class SettingSkills(models.Model):
    setting = models.ForeignKey(Setting, on_delete=models.CASCADE, null=True)
    setting_skill = models.CharField(max_length=1500, null=False, blank=False)
    percentage = models.CharField(max_length=150, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.setting_skill

    class Meta:
        ordering = ['setting_skill']


class Slider(models.Model):
    STATUS = (
        ('True', 'Enable'),
        ('False', 'Disable'),
    )
    group = models.CharField(max_length=150, null=False, verbose_name="Group", unique=True)
    status = models.CharField(max_length=10, choices=STATUS)
    title = models.CharField(max_length=150, null=False, verbose_name="Title", unique=True)
    sort_order = models.IntegerField(default=0, null=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def status_verbose(self):
        return dict(Slider.STATUS)[self.status]


class SliderMedia(models.Model):
    id = models.AutoField(primary_key=True)
    slider_id = models.ForeignKey(Slider, on_delete=models.CASCADE)
    media_type_choice = ((1, "Image"), (2, "Video"))
    media_type = models.CharField(max_length=255)
    media_content = models.FileField(upload_to='images/slider')
    media_link = models.URLField(null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Banners(models.Model):
    STATUS = (
        ('True', 'Enable'),
        ('False', 'Disable'),
    )
    Position = (
        ('Top Left', 'Top Left'),
        ('Top Middle', 'Top Middle'),
        ('Top Right', 'Top Right'),
        ('Middle Left', 'Middle Left'),
        ('Middle Right', 'Middle Right'),
        ('Bottom Left', 'Bottom Left'),
        ('Bottom Middle', 'Bottom Middle'),
        ('Bottom Right', 'Bottom Right'),
        ('Collection Sidebar', 'Collection Sidebar'),
        ('Categories Top', 'Categories Top'),
        ('Categories Sidebar', 'Categories Sidebar'),
    )

    status = models.CharField(max_length=10, choices=STATUS, default="True")
    position = models.CharField(max_length=150, null=False, choices=Position, unique=True)
    media_content = models.FileField(upload_to='images/banners/%Y/%m/')
    media_link = models.URLField(null=False, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.position.title


class Menu(models.Model):
    title = models.CharField(max_length=20, unique=True, )
    is_active = models.PositiveSmallIntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class MenuItems(MPTTModel):
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)
    type = models.CharField(max_length=20, )
    url = models.CharField(max_length=20, null=True)
    target = models.CharField(max_length=20, )
    position = models.IntegerField(null=True, )
    is_root = models.PositiveSmallIntegerField(default=0)
    is_fluid = models.PositiveSmallIntegerField(default=0)
    is_active = models.PositiveSmallIntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
