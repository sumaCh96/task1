from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    cost_per_item = models.FloatField()
    stock_quantity = models.IntegerField()
    volume = models.IntegerField()

    # def __str__(self):
    #     return (
    #         self.name, self.description, self.cost_per_item,
    #         self.stock_quantity, self.volume
    #     )
