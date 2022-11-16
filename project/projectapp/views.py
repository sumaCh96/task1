from django.shortcuts import render
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product
from .serializers import Product_serializer
# Create your views here.

class Prod(viewsets.ModelViewSet):
    queryset = Product.objects.all().values('name','costperitem','stockquantity','volume')
    serializer_class = Product_serializer

    def create(self, request, *args, **kwargs):
        try:
            data = request.data
            cost = data.get('costperitem')
            quantity = data.get('stockquantity')
            name = data.get('name')
            print(name)
            print(cost)
            print(quantity)
            volume = int(cost)*int(quantity)
            pr = Product.objects.create(
                costperitem = cost,
                stockquantity = quantity,
                volume = volume,
                name = name,
                )
            ser = self.get_serializer(pr).data
            return Response(
                data = {
                    'msg': 'succesfuly completed',
                    'details': ser,
                    'success':True,

                },
                status=status.HTTP_200_OK,

                )
        except Exception as error:
            return Response('invalid')