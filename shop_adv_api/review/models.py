from django.db import models
from shop.models import Shop
from user.models import User

# Create your models here.


class Review(models.Model):
    stars = models.IntegerField()
    content = models.CharField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='shop')