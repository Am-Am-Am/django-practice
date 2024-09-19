from django.contrib import admin

# Register your models here.
from goods.models import Categories, Products


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'quantity', 'price', 'discount']
    list_editable = ['quantity', 'price', 'discount']
    search_fields = ['name', 'description']
    list_filter = ['quantity', 'price', 'discount']
    fields = ['name', 'category', 'slug', 'description', 'image', ('price', 'discount'), 'quantity',]


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name',]