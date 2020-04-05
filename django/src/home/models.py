from django.db import models
from django.contrib.auth.models import User

class Video(models.Model):
    #User Powered
    title = models.CharField(max_length=50)
    videofile = models.FileField(upload_to='videos/%Y/%m/%d/', null=True, verbose_name="")
    tags = models.CharField(max_length=50, blank=True)
    
    #Generated
    location = models.CharField(max_length=500, blank=False)
    like_count = models.IntegerField(null=True, blank=True)
    view_count = models.IntegerField(null=True, blank=True)
    thumbnail = models.ImageField()
    author = models.CharField(max_length=150)
    date_of_upload = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title + ": " + str(self.videofile)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
