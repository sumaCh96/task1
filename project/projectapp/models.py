from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(null=False)
    costperitem = models.FloatField(default=0)
    stockquantity = models.IntegerField(default=0)
    volume = models.FloatField(blank=True,null=False)

