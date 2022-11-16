from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=30)
    Description = models.TextField()
    item_cost= models.IntegerField(default=0)
    stock_quantity=models.IntegerField(default=0)
    volume=models.PositiveIntegerField(blank=True)

    
