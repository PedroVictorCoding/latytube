from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from accounts.models import Account
from home.models import Video

class PostVisualization(models.Model):
    post_id     = models.ForeignKey(Video, on_delete=models.CASCADE)
    from_user   = models.ForeignKey(Account, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.post_id.title + " - Viewed by: " + self.from_user.username + " - User pk: " + str(self.from_user.pk)

class PostLike(models.Model):
    post_id     = models.ForeignKey(Video, on_delete=models.CASCADE)
    from_user   = models.ForeignKey(Account, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.post_id.title + " - Liked by: " + self.from_user.username + " - User pk: " + str(self.from_user.pk)