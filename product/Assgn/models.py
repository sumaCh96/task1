from django.db import models

# Create your models here.


class Products(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    item_cost = models.FloatField()
    stock_quantity = models.IntegerField()
    volume = models.PositiveIntegerField()

