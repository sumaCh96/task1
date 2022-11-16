from rest_framework.serializers import ModelSerializer

from.models import Products


class Prod_serializ(ModelSerializer):
    class Meta:
        model=Products
        fields='__all__'
