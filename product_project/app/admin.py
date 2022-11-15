from django.contrib import admin
from .models import Product


# Register your models here.
class AdminProduct(admin.ModelAdmin):
    list_display = [
                    'name', 'cost_per_item',
                    'stock_quantity', 'volume'
                   ]


admin.site.register(Product, AdminProduct)
