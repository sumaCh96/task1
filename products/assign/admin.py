from django.contrib import admin

from .models import Product


# Register your models here.
class ProAdmin(admin.ModelAdmin):
    list_display = ['name','item_cost','stock_quantity','volume']


admin.site.register(Product,ProAdmin)