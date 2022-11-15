from django.db import models

# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=False)
    cost_per_item = models.FloatField()
    stock_quantity = models.IntegerField()
    volume = models.IntegerField()

