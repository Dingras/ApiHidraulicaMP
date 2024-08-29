from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, null=False)
    url_img = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=200, null=True)
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    price = models.DecimalField(max_digits=12, decimal_places=2, null=False)
    count = models.IntegerField(default=0)
    url_img = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name
