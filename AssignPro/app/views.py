from django.shortcuts import render
from rest_framework import viewsets, generics, permissions, status
from rest_framework.response import Response

from .models import product
from .serializers import product_serializer



class productcrud(viewsets.ModelViewSet):
    queryset = product.objects.all()
    serializer_class = product_serializer



    def create(self,request,*args,**kwargs):
        try:
            data=request.data
            name=data.get('name',None)
            # description = data.get('description',None)
            cost_per_item =data.get('cost_per_item',None)
            stock_quantity =data.get('stock_quantity',None)
            volume =int(cost_per_item)*int(stock_quantity)
            pro=product.objects.create(
            name=name,
            # description=('description',None),
            cost_per_item= cost_per_item,
            stock_quantity= stock_quantity,
            volume =volume
            )
            serializer_data = self.get_serializer(pro).data

            return Response(
                data={
                "message": "Details added successfully",
                "details": serializer_data,
                "success": 'True'

                },
            status=status.HTTP_201_CREATED
             )

        except Exception as error:

            return Response(
            {"message": str(error)}, status=status.HTTP_400_BAD_REQUEST
            )