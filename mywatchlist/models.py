from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class WatchlistItem(models.Model):
    # WATCHED = 'Watched'
    # NEVER_WATCHED = 'Have Not Watched'

    # WATCHED_OR_NOT = [
    #     (WATCHED, 'Watched'), 
    #     (NEVER_WATCHED, 'Have Not Watched'), 
    # ]
    # watched = models.CharField(
    #     max_length=20, 
    #     choices=WATCHED_OR_NOT, 
    #     default=NEVER_WATCHED,
    # )
    watched = models.TextField()
    title = models.TextField()
    rating = models.FloatField()
    release_date=models.DateField()
    review = models.TextField()