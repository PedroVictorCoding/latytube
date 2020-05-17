from django.db import models
from django.contrib.auth.models import User
from accounts.models import Account
import uuid
from django_countries.fields import CountryField
from django.core.validators import MaxValueValidator, MinValueValidator


def generated_filename(instance, filename):
    extension = filename.split('.')[-1]
    generated = uuid.uuid4()
    return '{}{}.{}'.format('videos/', str(generated), extension)


skins_available = (
    ('standard', 'Standard'),
    ('flag_corner', '🇺🇸 Country Flag'),
    ('fire_emoji', '🔥 Fire Emoji'),
    ('rainbow_overlay', '🏳️‍🌈 Rainbow Overlay ')
)

class Video(models.Model):
    #User Powered
    title               = models.CharField(max_length=50)
    videofile           = models.FileField(upload_to=generated_filename, null=True, verbose_name="")
    tags                = models.CharField(max_length=50, blank=True)
    country_of_upload   = CountryField()
    video_skin          = models.CharField(choices=skins_available, default="standard", max_length=50)
    
    #Generated
    longitude       = models.FloatField(blank=False)
    latitude        = models.FloatField(blank=False)
    like_count      = models.IntegerField(null=True, blank=True)
    view_count      = models.IntegerField(null=True, blank=True)
    author          = models.ForeignKey(Account, on_delete=models.CASCADE)
    date_of_upload  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + ": " + str(self.videofile) + ": " + str(self.id)
        return self.author.username

    