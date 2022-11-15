from django.contrib import admin

from taskapp.models import Products


# Register your models here.

class ProductView(admin.ModelAdmin):
    list_display = ['name','description','cost_per_item','quantity']

admin.site.register(Products,ProductView)