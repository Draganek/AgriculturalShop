from django.db import models
from products.models import Product
from users.models import Client

# Create your models here.
class Order(models.Model):
    order_number = models.CharField(max_length=120)
    item = models.ForeignKey(Product, on_delete=models.CASCADE,)
    models.DecimalField(max_digits=15,decimal_places = 2, default=99.99)
    date = models.DateField()