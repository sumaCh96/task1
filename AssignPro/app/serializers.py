
from rest_framework.serializers import ModelSerializer

from .models import product


class product_serializer(ModelSerializer):
    class Meta:
        model = product
        fields=[
                'name', 'cost_per_item', 'stock_quantity', 'volume'
               ]