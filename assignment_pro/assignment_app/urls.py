from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from .views import ProductsCurd


router = routers.DefaultRouter()
router.register(r"dis",ProductsCurd,basename="dis")

urlpatterns = [
    path('',include(router.urls)),

]