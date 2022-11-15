

from django.urls import path, include
from rest_framework import routers

from .views import ProductDetails

router = routers.DefaultRouter()


router.register(r'pro', ProductDetails, basename='pro')

urlpatterns = [
    path('', include(router.urls)),
]
