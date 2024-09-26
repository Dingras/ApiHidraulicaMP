from django.db import models
from Products.models import Product

# Create your models here.
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()


# class Sale(models.Model):
#     # client = models.ForeignKey(Client, on_delete=models.CASCADE)
#     date = models.DateTimeField(auto_now_add=True)
#     total = models.DecimalField(max_digits=12, decimal_places=2)

#     def __str__(self):
#         return f"Venta Nro.: {self.id} - Fecha: {self.date}" # - Cliente: {self.client}

# class SaleItem(models.Model):
#     sale = models.ForeignKey(Sale, related_name='items', on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.IntegerField()
#     price = models.DecimalField(max_digits=12, decimal_places=2)

#     def __str__(self):
#         return f"{self.quantity} x {self.producto.nombre}"