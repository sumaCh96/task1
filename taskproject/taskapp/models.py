from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    cost_per_item = models.FloatField()
    quantity = models.IntegerField()
    volume = models.IntegerField()




