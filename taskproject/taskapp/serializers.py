from rest_framework.serializers import ModelSerializer

from taskapp.models import Products


class ProductSerializers(ModelSerializer):
    class Meta:
        model = Products
        fields = ['name','cost_per_item','quantity', 'volume']


