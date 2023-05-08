from django.contrib import admin
from .models import *


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class CategoryOrder(admin.ModelAdmin):
    list_display = ['product', 'customer', 'status']

class CategoryCustomer(admin.ModelAdmin):
    list_display = ['first_name', 'phone', 'email']

# Register your models here.
admin.site.register(Products,AdminProduct)
admin.site.register(Category)
admin.site.register(Customer, CategoryCustomer)
admin.site.register(Order, CategoryOrder)