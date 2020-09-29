from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager
from django.conf import settings
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
import uuid

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email")

        if not username:
            raise ValueError("Users must have an email")

        user = self.model(
            username = username,
            email = self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            username = username,
            email = self.normalize_email(email),
            password = password,
        )
        user.is_admin        = True
        user.is_staff        = True
        user.is_superuser    = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    username            = models.CharField(max_length=30, unique=True)
    email               = models.EmailField(max_length=50, verbose_name="email", unique=True)
    date_joined         = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login          = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin            = models.BooleanField(default=False)
    is_active           = models.BooleanField(default=True)
    is_staff            = models.BooleanField(default=False)
    is_superuser        = models.BooleanField(default=False)
    signup_confirmation = models.BooleanField(default=False)

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True

    def is_staff(self):
        return self.is_admin


@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
    

def generated_filename(instance, filename):
    extension = filename.split('.')[-1]
    generated = uuid.uuid4()
    return '{}{}.{}'.format('profile-images/', str(generated), extension)


class UserProfile(models.Model):
    user            = models.OneToOneField(Account, on_delete=models.CASCADE)
    display_name    = models.CharField(max_length=25)
    bio             = models.CharField(blank=True, max_length=200)
    image           = models.ImageField(blank=True, upload_to=generated_filename)
    latitude        = models.FloatField(blank=True, null=True)
    longitude       = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=Account)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


