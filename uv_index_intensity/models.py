from django.db import models

# Create your models here.
class Data(models.Model):
    uvIntensity = models.CharField(max_length=10, blank=True, default='')
    uvIndex = models.CharField(max_length=10, blank=True, default='')