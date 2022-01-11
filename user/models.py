from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, User, AbstractUser, Permission, Group
from django.db import models, IntegrityError
from django.utils.safestring import mark_safe
from django.utils.text import slugify


class UserManager(BaseUserManager):
    def create_user(self, email, first_name=None, last_name=None, password=None, username="", is_active=True,
                    is_staff=False
                    , is_author=False, is_admin=False, is_superuser=False, ):

        if not email:
            raise ValueError("users must have an email address")
        # Validate email is unique in database
        if User.objects.filter(email=self.normalize_email(email).lower()).exists():
            raise ValueError('This email has already been registered.')

        user_obj = self.model(
            email=self.normalize_email(email).lower(),
            first_name=first_name,
            last_name=last_name,
        )
        user_obj.set_password(password)
        user_obj.author = is_author
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.is_superuser = is_superuser
        # Save and catch IntegrityError (due to email being unique)
        try:
            user_obj.save(using=self._db)

        except IntegrityError:
            raise ValueError('This email has already been registered.')

        return user_obj

    def create_staff_user(self, email, first_name=None, last_name=None, password=None):
        return self.create_user(
            email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            is_staff=True,
        )

    def create_superuser(self, email, first_name=None, last_name=None, password=None):
        return self.create_user(
            email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            is_staff=True,
            is_admin=True,
            is_superuser=True,
        )


class User(AbstractBaseUser):
    """
    Description:This is going to be the main User Model
    """

    email = models.EmailField(verbose_name='email address', max_length=255, unique=True, error_messages={
        'unique': "This email has already been registered.",
    })
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='images/users/%y/%m', default='images/users/digithup-user.png')
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    is_author = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    objects = UserManager()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.email)
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.email

    def get_full_name(self):
        full_name = None
        if self.first_name or self.last_name:
            return self.first_name + " " + self.last_name
        else:
            return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def has_perm(self, perm, obj=None):
        # Does the user have a specific permission?
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        # "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_admin(self):
        # "Is the user an admin member?"
        return self.is_admin

    # @property
    # def is_active(self):
    #     "Is the user active?"
    #     return self.active

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'Image'
