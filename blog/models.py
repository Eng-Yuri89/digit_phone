import logging

from django.conf import settings
from django.core.cache import cache
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from tinymce.models import HTMLField

from core.utils.utils import cache_decorator
from helper.modelHelper import STATUS

logger = logging.getLogger(__name__)


class LinkShowType(models.TextChoices):
    I = ('i', 'front page')
    L = ('l', 'List')
    P = ('p', 'Article page')
    A = ('a', 'Full Site')
    S = ('s', 'Friendship link page')


#
# class BaseModel(models.Model):
#     id = models.AutoField(primary_key=True)
#     created_time = models.DateTimeField('Creation time', default=now)
#     last_mod_time = models.DateTimeField('Change the time', default=now)
#
#     def save(self, *args, **kwargs):
#         is_update_views = isinstance(
#             self,
#             Article) and 'update_fields' in kwargs and kwargs['update_fields'] == ['views']
#         if is_update_views:
#             Article.objects.filter(pk=self.pk).update(views=self.views)
#         else:
#             if 'slug' in self.__dict__:
#                 slug = getattr(
#                     self, 'title') if 'title' in self.__dict__ else getattr(
#                     self, 'name')
#                 setattr(self, 'slug', slugify(slug))
#             super().save(*args, **kwargs)
#
#     def get_full_url(self):
#         site = get_current_site().domain
#         return "https://{site}{path}".format(site=site,
#                                             path=self.get_absolute_url())
#
#     class Meta:
#         abstract = True
#
#     @abstractmethod
#     def get_absolute_url(self):
#         pass


class Article(models.Model):
    """article"""
    STATUS_CHOICES = (
        ('Draft', 'Draft'),
        ('Publish', 'Publish'),
    )
    COMMENT_STATUS = (
        ('Open', 'Open'),
        ('Close', 'Close'),
    )
    TYPE = (
        ('Article', 'Article'),
        ('Page', 'Page'),
    )
    title = models.CharField(max_length=255, unique=True)
    keyword = models.CharField(max_length=255, null=False, blank=False, default='')
    body = HTMLField(blank=True, default='', null=True)
    pub_time = models.DateTimeField(
        'release time', blank=False, null=False, default=now)
    status = models.CharField(
        'Article status',
        max_length=10,
        choices=STATUS_CHOICES,
        default='Draft')
    image = models.ImageField(upload_to='images/article/%Y/%m', default='images/Ydoob.png')
    is_featured = models.CharField(max_length=255, choices=STATUS, default='Inactive')
    comment_status = models.CharField(
        'Comment status',
        max_length=10,
        choices=COMMENT_STATUS,
        default='Close')
    type = models.CharField('type', max_length=10, choices=TYPE, default='Article')
    views = models.PositiveIntegerField('Pageviews', default=0)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='author',
        blank=False,
        null=False,
        on_delete=models.CASCADE)
    article_order = models.IntegerField(
        'Sort, the higher the number, the higher the front', blank=False, null=False, default=0)
    show_toc = models.BooleanField(" display the toc ", blank=False, null=False, default=False)
    category = models.ForeignKey(
        'Category',
        verbose_name='Classification',
        on_delete=models.CASCADE,
        blank=False,
        null=False)
    tags = models.ManyToManyField('Tag', verbose_name='tag collection', blank=True)
    slug = models.SlugField(unique=True)
    create_at = models.DateTimeField(auto_now=True, null=False)
    update_at = models.DateTimeField(auto_now=True)

    def body_to_string(self):
        return self.body

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-article_order', '-pub_time']
        verbose_name = "article"
        verbose_name_plural = verbose_name
        get_latest_by = 'id'

    def save(self, *args, **kwargs):

        is_update_views = isinstance(
            self,
            Article) and 'update_fields' in kwargs and kwargs['update_fields'] == ['views']
        if is_update_views:
            Article.objects.filter(pk=self.pk).update(views=self.views)
        else:
            if 'slug' in self.__dict__:
                slug = getattr(
                    self, 'title') if 'title' in self.__dict__ else getattr(
                    self, 'name')
                setattr(self, 'slug', slugify(slug))
            super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:detailbyid', kwargs={
            'article_id': self.id,
            'year': self.update_at.year,
            'month': self.update_at.month,
            'day': self.update_at.day
        })

    @cache_decorator(60 * 60 * 10)
    def get_category_tree(self):
        tree = self.category.get_category_tree()
        names = list(map(lambda c: (c.name, c.get_absolute_url()), tree))

        return names

    def viewed(self):
        self.views += 1
        self.save(update_fields=['views'])

    def comment_list(self):
        cache_key = 'article_comments_{id}'.format(id=self.id)
        value = cache.get(cache_key)
        if value:
            logger.info('get article comments:{id}'.format(id=self.id))
            return value
        else:
            comments = self.comment_set.filter(is_enable=True)
            cache.set(cache_key, comments, 60 * 100)
            logger.info('set article comments:{id}'.format(id=self.id))
            return comments

    def get_admin_url(self):
        info = (self._meta.app_label, self._meta.model_name)
        return reverse('admin:%s_%s_change' % info, args=(self.pk,))

    @cache_decorator(expiration=60 * 100)
    def next_article(self):
        # Next
        return Article.objects.filter(
            id__gt=self.id, status='p').order_by('id').first()

    @cache_decorator(expiration=60 * 100)
    def prev_article(self):
        # Previous Article
        return Article.objects.filter(id__lt=self.id, status='p').first()


class Category(models.Model):
    """category"""
    name = models.CharField('name', max_length=30, unique=True)
    parent_category = models.ForeignKey(
        'self',
        verbose_name="article category",
        blank=True,
        null=True,
        on_delete=models.CASCADE)
    slug = models.SlugField(default='no-slug', max_length=60, blank=True)
    index = models.IntegerField(default=0, verbose_name="category index")
    create_at = models.DateTimeField(auto_now=True, null=False)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-index']
        verbose_name = "category"
        verbose_name_plural = verbose_name

    def get_absolute_url(self):
        return reverse(
            'blog:category_detail', kwargs={
                'category_name': self.slug})

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    @cache_decorator(60 * 60 * 10)
    def get_category_tree(self):
        """
        Recursively get the parent of the category
        :return:
        """
        categorys = []

        def parse(category):
            categorys.append(category)
            if category.parent_category:
                parse(category.parent_category)

        parse(self)
        return categorys

    @cache_decorator(60 * 60 * 10)
    def get_sub_categorys(self):
        """
        Get all subsets of the current category
        :return:
        """
        categorys = []
        all_categorys = Category.objects.all()

        def parse(category):
            if category not in categorys:
                categorys.append(category)
            childs = all_categorys.filter(parent_category=category)
            for child in childs:
                if category not in categorys:
                    categorys.append(child)
                parse(child)

        parse(self)
        return categorys


class Tag(models.Model):
    """Article tags"""
    name = models.CharField('tag', max_length=30, unique=True)
    slug = models.SlugField(default='no-slug', max_length=60, blank=True)
    create_at = models.DateTimeField(auto_now=True, null=False)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:tag_detail', kwargs={'tag_name': self.slug})

    @cache_decorator(60 * 60 * 10)
    def get_article_count(self):
        return Article.objects.filter(tags__name=self.name).distinct().count()

    class Meta:
        ordering = ['name']
        verbose_name = "article tags"
        verbose_name_plural = verbose_name


class Links(models.Model):
    """Links"""

    name = models.CharField('Link name', max_length=30, unique=True)
    link = models.URLField('link address')
    sequence = models.IntegerField('sort', unique=True)
    is_enable = models.BooleanField(
        'link enable', default=True, blank=False, null=False)
    show_type = models.CharField(
        'Display type',
        max_length=1,
        choices=LinkShowType.choices,
        default=LinkShowType.I)
    created_time = models.DateTimeField('Creation time', default=now)
    last_mod_time = models.DateTimeField('Change the time', default=now)

    class Meta:
        ordering = ['sequence']
        verbose_name = 'links'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class SideBar(models.Model):
    """Sidebar, you can display some html content"""
    name = models.CharField('name', max_length=100)
    content = models.TextField("content")
    sequence = models.IntegerField('sort', unique=True)
    is_enable = models.BooleanField('sidebar enable', default=True)
    created_time = models.DateTimeField('created time', default=now)
    last_mod_time = models.DateTimeField('modfiy time', default=now)

    class Meta:
        ordering = ['sequence']
        verbose_name = 'sidebar'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class BlogSettings(models.Model):
    '''BlogSettings '''
    sitename = models.CharField(
        "Site name",
        max_length=200,
        null=False,
        blank=False,
        default='')
    site_description = models.TextField(
        "Site description",
        max_length=1000,
        null=False,
        blank=False,
        default='')
    site_seo_description = models.TextField(
        "Website SEO description", max_length=1000, null=False, blank=False, default='')
    site_keywords = models.TextField(
        "Site keywords",
        max_length=1000,
        null=False,
        blank=False,
        default='')
    article_sub_length = models.IntegerField("Article summary length", default=300)
    sidebar_article_count = models.IntegerField("Number of sidebar articles", default=10)
    sidebar_comment_count = models.IntegerField("comment count", default=5)
    show_google_adsense = models.BooleanField('Number of sidebar comments', default=False)
    google_adsense_codes = models.TextField(
        'Advertising content', max_length=2000, null=True, blank=True, default='')
    open_site_comment = models.BooleanField('open site comment', default=True)
    beiancode = models.CharField(
        'record number',
        max_length=2000,
        null=True,
        blank=True,
        default='')
    analyticscode = models.TextField(
        "Website Statistics Code",
        max_length=1000,
        null=False,
        blank=False,
        default='')
    show_gongan_code = models.BooleanField(
        '是否显示公安备案号', default=False, null=False)
    gongan_beiancode = models.TextField(
        'gongan beiancode',
        max_length=2000,
        null=True,
        blank=True,
        default='')
    resource_path = models.CharField(
        "resource path",
        max_length=300,
        null=False,
        default='/var/www/resource/')

    class Meta:
        verbose_name = 'blog setting'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.sitename

    def clean(self):
        if BlogSettings.objects.exclude(id=self.id).count():
            raise ValidationError(_('There can only be one configuration'))

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        from core.utils.utils import cache
        cache.clear()
