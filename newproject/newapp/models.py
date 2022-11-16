from django.db import models


# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=10)
    cost_per_item = models.IntegerField()
    stock_quantity = models.IntegerField()
    volume = models.IntegerField()

    def __str__(self):
        return self.volume, self.name, self.stock_quantity, self.cost_per_item, self.description
