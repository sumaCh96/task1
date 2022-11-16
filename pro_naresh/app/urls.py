from django.contrib import admin
from django.urls import path,include

from rest_framework import  routers
router = routers.DefaultRouter()
from .views import ProductsCrud

router.register(r"pro",ProductsCrud,basename="pro")

urlpatterns=[
    path('',include(router.urls)),
]


