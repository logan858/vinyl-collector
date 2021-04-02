from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class StoreTwo(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Vinyl(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    release = models.IntegerField()
    def __str__(self):
        return self.title
    def listen_count(self):
        return len(self.listen_set.all())
    stores = models.ManyToManyField(StoreTwo)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Listen(models.Model):
  date = models.DateField()
  track = models.CharField(max_length=10)
  vinyl = models.ForeignKey(Vinyl, on_delete=models.CASCADE)
  def __str__(self):
      return f"{self.track} on {self.date}"
  class Meta:
      ordering= ['-date']