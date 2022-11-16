from django.shortcuts import render
from rest_framework import viewsets,status
from .models import Products
from .serializers import Prod_Serializ
from rest_framework.response import Response


# Create your views here.
class ProductsCurd(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = Prod_Serializ

    def create(self, request, *args, **kwargs):
        try:
            data = request.data
            name = data.get('name')
            cost = data.get('cost')
            stock_qty = data.get('stock_qty')
            volume = int(cost)*int(stock_qty)

            pro_record = Products.objects.create(
                name = name,
                cost = cost,
                stock_qty = stock_qty,
                volume = volume

            )

            serial = self.get_serializer(pro_record).data

            return Response(
                data={
                    'message':"Successfully Done",
                    'details':serial,
                    'success':True
                }, status=status.HTTP_201_CREATED
            )
        except Exception as Error:
            return Response(
                data={
                    'message':'not found'
                },status=status.HTTP_400_BAD_REQUEST
            )



