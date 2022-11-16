from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializers


# Create your views here.
class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    def create(self, request, *args, **kwargs):
        try:
            data = request.data
            name = data.get('name', None)
            item_cost = data.get('item_cost', None)
            stock_quantity = data.get('stock_quantity', None)
            volume = int(item_cost) * int(stock_quantity)
            productt = Product.objects.create(
                name=name,
                item_cost=item_cost,
                stock_quantity=stock_quantity,
                volume=volume
            )
            serializer = self.get_serializer(productt).data
            return Response(data={
                'message': 'Succussfully Completed',
                'details': serializer,
                'success': True,
            },
                status=status.HTTP_200_OK,
            )
        except Exception as exp:
            return Response('Invalid')
