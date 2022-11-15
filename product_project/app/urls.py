from django.urls import path, include
from rest_framework import routers

from .views import products

router = routers.DefaultRouter()

router.register(r"product", products, basename="product")

urlpatterns = [
    path("", include(router.urls))
]
