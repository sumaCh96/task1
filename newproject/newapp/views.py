from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets, status
from .serializer import Productserializer
from .models import product
from rest_framework.response import Response


class Product(viewsets.ModelViewSet):
    queryset = product.objects.all()
    serializer_class = Productserializer

    def create(self, request, volume=None, *args, **kwargs):

        try:
            data = request.data
            product_name = data.get('name', None)
            product_item_cost = data.get('cost_per_item', None)
            product_stock_quantity = data.get('stock_quantity', None)

            volume = int(product_item_cost) * int(product_stock_quantity)

            Product = product.objects.create(
                name=product_name,
                cost_per_item=product_item_cost,
                stock_quantity=product_stock_quantity,
                volume=volume
            )

            serializer = self.get_serializer(Product).data
            return Response(
                data={
                    "message": "Successfully Done",
                    "details": serializer
                },
                status=status.HTTP_200_OK
            )
        except Exception as error:
            return Response(status=status.Http_400_BAD_REQUEST)
