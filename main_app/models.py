from django.db import models

# Create your models here.

class Vinyl(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    release = models.IntegerField()
    def __str__(self):
        return self.title