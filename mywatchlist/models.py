from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class WatchlistItem(models.Model):
    watched = models.TextField()
    title = models.TextField()
    rating = models.FloatField()
    release_date=models.DateField()
    review = models.TextField()