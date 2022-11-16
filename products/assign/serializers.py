from rest_framework.serializers import ModelSerializer

from .models import Product


class ProductSerializers(ModelSerializer):
    class Meta:
        model = Product
        fields =['name','item_cost','stock_quantity','volume']