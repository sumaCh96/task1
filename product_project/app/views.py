from django.shortcuts import render
from rest_framework import viewsets, status
from .serializer import ProductSerializer
from .models import Product
from rest_framework.response import Response


# Create your views here.

class products(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):

        try:
            data = request.data
            product_name = data.get('name', None)
            product_item_cost = data.get('cost_per_item', None)
            product_stock_quantity = data.get('stock_quantity', None)

            volume = int(product_item_cost)*int(product_stock_quantity)

            product = Product.objects.create(
                name=product_name,
                cost_per_item=product_item_cost,
                stock_quantity=product_stock_quantity,
                volume=volume
            )

            serializer = self.get_serializer(product).data
            return Response(
                data={
                    "message": "Successfully Done",
                    "details": serializer,
                    "Sucees": True
                },
                status=status.HTTP_200_OK
            )
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)
