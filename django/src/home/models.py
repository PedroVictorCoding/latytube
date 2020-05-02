from django.db import models
from django.contrib.auth.models import User
from accounts.models import Account
import uuid
from django_countries.fields import CountryField

##countries = dict(countries_for_language('en'))
##
##countries_tuple = countries.items()
### countries_tuple = [(v, k) for k, v in countries.items()]


def generated_filename(instance, filename):
    extension = filename.split('.')[-1]
    generated = uuid.uuid4()
    return '{}{}.{}'.format('videos/', str(generated), extension)



class Video(models.Model):
    #User Powered
    title               = models.CharField(max_length=50)
    videofile           = models.FileField(upload_to=generated_filename, null=True, verbose_name="")
    tags                = models.CharField(max_length=50, blank=True)
    country_of_upload   = CountryField()
    
    #Generated
    longitude       = models.CharField(max_length=500, blank=False)
    latitude        = models.CharField(max_length=500, blank=False)
    like_count      = models.IntegerField(null=True, blank=True)
    view_count      = models.IntegerField(null=True, blank=True)
    author          = models.ForeignKey(Account, on_delete=models.CASCADE)
    date_of_upload  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + ": " + str(self.videofile) + ": " + str(self.id)
        return self.author.username

    