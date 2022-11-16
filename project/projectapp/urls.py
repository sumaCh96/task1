from django.urls import path,include
from rest_framework import routers
from .views import Prod
router = routers.DefaultRouter()
router.register(r'pr',Prod,basename='product')

urlpatterns = [
    path('',include(router.urls))
]