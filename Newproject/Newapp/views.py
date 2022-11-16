from django.core.serializers import get_serializer
from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response

from Newapp.models import Products
from Newapp.serilizers import Prod_serializ

# Create your views here.



class ProductsCrud(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = Prod_serializ


    def create(self, request, *args, **kwargs):
        data=request.data
        try:

            name=data.get('name',None)
            description=data.get('description',None)
            cost=data.get('cost',None)
            stock_qty= data.get('stock_qty',None)
            valume= int(cost)*int(stock_qty)

            products_record=Products.objects.create(
                 name=name,
                 description=description,
                 cost=cost,
                 stock_qty=stock_qty,
                 volume=volume
            )

            serializer_data=get_serializer(products_record).data

            return Response(
                 data={
                 "message":"Details Added Successfully",
                 "details":serializer_data,
                 "success":True
                 }
            )
        except Exception as error:
              return Response({'message':str(error)},status.HTTP_400_BAD_REQUEST)







