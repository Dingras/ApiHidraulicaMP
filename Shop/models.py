from django.db import models
from django.contrib.auth.models import User
from Products.models import Product

# Create your models here.
class CartItem(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
