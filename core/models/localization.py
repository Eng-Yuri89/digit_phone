from django.db import models


# Create your models here.
from django.template.defaultfilters import slugify

from helper.modelHelper import USER_STATUS, STATUS


class Home(models.Model):
    title = models.CharField(max_length=10,default='Nigne')
    content = models.CharField(max_length=300,default="")
    slug = models.SlugField(max_length=30, unique=True,default='nigne')


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Home, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Language(models.Model):
    name = models.CharField(max_length=20, unique=True, default='English')
    code = models.CharField(max_length=5, unique=True,default='en')
    image = models.ImageField(upload_to='images/lang/%Y/%m/%d', null=True, default='images/lang/en-gb.png')
    status = models.CharField(max_length=20, choices=USER_STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Currency(models.Model):
    name = models.CharField(max_length=20, unique=True, default='Egypt Pound')
    code = models.CharField(max_length=5, unique=True,default='EGP')
    exchange= models.DecimalField(max_digits=8, decimal_places=2, default=6.99, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS,unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.code


from django.db import models
from django.utils.text import slugify


class Country(models.Model):
    name = models.CharField(max_length=30,default='Egypt')
    name_ar = models.CharField(max_length=30,default='مصر')
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Country, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Governorates(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=30,default='Qena')
    name_ar = models.CharField(max_length=30,default='قنا')
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Governorates, self).save(*args, **kwargs)
    def __str__(self):
        return self.name


class City(models.Model):
    governorates = models.ForeignKey(Governorates, on_delete=models.CASCADE)
    name = models.CharField(max_length=50,default='Qena')
    name_ar = models.CharField(max_length=50,default='Qena')
    slug = models.SlugField(unique=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(City, self).save(*args, **kwargs)
    def __str__(self):
        return self.name



class Area(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=30,default='Qena')
    name_ar = models.CharField(max_length=30,default='Qena')
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Area, self).save(*args, **kwargs)
    def __str__(self):
        return self.name



