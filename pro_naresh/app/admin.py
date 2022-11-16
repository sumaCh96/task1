from django.contrib import admin
from .models import Products


class productAdmin(admin.ModelAdmin):
    list_display = ["name",'cost', 'stock_qty', 'volume']

admin.site.register(Products,productAdmin)