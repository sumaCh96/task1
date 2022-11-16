from rest_framework.serializers import ModelSerializer
from .models import Products


class Prod_Serializ(ModelSerializer):
    class Meta:
         model = Products
         fields = ['name','cost','stock_qty','volume']
