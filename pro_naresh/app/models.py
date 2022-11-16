from django.db import models

# Create your models here.
class Products(models.Model):
    name=models.CharField(max_length=23)
    description=models.TextField(null=False)
    cost=models.FloatField()
    stock_qty=models.IntegerField()
    volume=models.IntegerField()


