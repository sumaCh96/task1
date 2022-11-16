from django.urls import include, path
from rest_framework import routers

from .views import ProductViewset

router = routers.DefaultRouter()

router.register(r"product", ProductViewset,basename='product')
urlpatterns = [
    path('', include(router.urls)),

]
