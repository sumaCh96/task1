from rest_framework.serializers import ModelSerializer
from .models import Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = [
                  'name', 'cost_per_item',
                  'stock_quantity', 'volume'
                  ]

