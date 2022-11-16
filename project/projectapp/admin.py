from django.contrib import admin
from projectapp.models import Product
# Register your models here.
class Product_list(admin.ModelAdmin):
    list_display = ['name','costperitem','stockquantity']

admin.site.register(Product,Product_list)
