from django.contrib import admin

from .models import Products


# Register your models here.


class ProductView(admin.ModelAdmin):
    list_display = ['name', 'item_cost', 'stock_quantity', 'volume']


admin.site.register(Products, ProductView)