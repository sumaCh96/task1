from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'stock_quantity','cost_per_item','volume']


admin.site.register(product, ProductAdmin)

