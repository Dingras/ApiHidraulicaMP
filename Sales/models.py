from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Sale(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"Venta Nro.: {self.id} - Fecha: {self.date}"

class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.name}"