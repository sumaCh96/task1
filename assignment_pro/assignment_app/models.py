from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    cost = models.FloatField()
    stock_qty = models.IntegerField()
    volume = models.FloatField()

    def __str__(self):
        return self.name,self.description,self.cost,self.stock_qty



