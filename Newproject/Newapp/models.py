from django.db import models

# Create your models here.
class Products(models.Model):
    name=models.CharField(max_length=23)
    description=models.CharField(max_length=30)
    cost=models.FloatField()
    stock_qty=models.IntegerField()
    valume=models.FloatField()


    def __str__(self):
        return self.name
