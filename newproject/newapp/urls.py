from django.urls import path,include
from rest_framework import routers


from .views import Product

router=routers.DefaultRouter()


router.register(r"product", Product, basename="product")

urlpatterns=[
    path("", include(router.urls))
]
