from django.contrib import admin

from app.models import product

# Register your models here.
class productadmin(admin.ModelAdmin):
    list_display = ['name','description','cost_per_item','stock_quantity','volume']
admin.site.register(product, productadmin)