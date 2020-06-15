from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from home.models import Video
from accounts.models import Account

class PostVisualization(models.Model):
    post_id     = models.ForeignKey(Video, on_delete=models.CASCADE)
    from_user   = models.ForeignKey(Account, on_delete=models.CASCADE)