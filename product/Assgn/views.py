
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Products
from .serializers import ProductSerializer


# Create your views here.

class ProductDetails(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        try:
           data = request.data
           name = data.get('name', None)
           description = data.get('description', None)
           item_cost = data.get('item_cost', None)
           stock_quantity = data.get('stock_quantity', None)
           volume = int(item_cost)*int(stock_quantity)

           product = Products.objects.create(

               name=name,
               item_cost=item_cost,
               stock_quantity=stock_quantity,
               volume=volume
           )
           serializer = self.get_serializer(product).data

           return Response(
               data={
                   'message': "successfully completed",
                   'details': serializer,
                   'success': True
               }, status=status.HTTP_201_CREATED
           )
        except Exception as Error:
            return Response(
                data={
                    'message': 'not found'
                }, status=status.HTTP_400_BAD_REQUEST)