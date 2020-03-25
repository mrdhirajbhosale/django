from django.db import models


# Create your models here.

class Shop(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=256)
    landmark = models.CharField(max_length=256)
    area = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    state = models.CharField(max_length=256)
    country = models.CharField(max_length=256)
    pin_code = models.CharField(max_length=6)
    contact = models.CharField(max_length=10)
    timing = models.CharField(max_length=50)
    category = models.CharField(max_length=20)
    poster = models.ImageField()
