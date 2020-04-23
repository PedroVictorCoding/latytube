from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Achievements(models.Model):
    share_link = models.IntegerField(
        blank=True,
        validators=[MaxValueValidator(10)] # Limit of actions
    )
