from django.core.serializers import get_serializer
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from taskapp.models import Products
from taskapp.serializers import ProductSerializers


# Create your views here.


class ProductsCrud(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializers


    def create(self, request, *args, **kwargs):
        data = request.data
        try:
            name = data.get('name',None)
            cost_per_item = data.get('cost_per_item',None)
            quantity = data.get('quantity',None)
            volume = int(cost_per_item)*int(quantity)


            products_record = Products.objects.create(
                name = name,
                cost_per_item = cost_per_item,
                quantity = quantity,
                volume = volume
            )

            serializer_data = get_serializer(products_record).data

            return Response(
                data = {
                "message":"Details Added Successfully",
                "details":serializer_data,
                "success":True
                }
            )

        except Exception as error:
            return Response({'message': str(error)}, status=status.HTTP_400_BAD_REQUEST)





