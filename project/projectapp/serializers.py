from rest_framework.serializers import ModelSerializer
from .models import Product

class Product_serializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('name','costperitem','stockquantity','volume')




