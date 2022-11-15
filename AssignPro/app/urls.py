from django.urls import path,include
from rest_framework import routers
router = routers.DefaultRouter()
from .views import productcrud
router.register(r'productcrud', productcrud, basename="productcrud")

urlpatterns =[
    path('',include(router.urls))

]