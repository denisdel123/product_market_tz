from django.contrib import admin

from marketApp.models import Category, Subcategory, Product, CartView


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['photo', 'name', 'slug']


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['photo', 'name', 'slug', 'associated_category']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['photo', 'name', 'price', 'slug', 'associated_subcategory']


@admin.register(CartView)
class CartViewAdmin(admin.ModelAdmin):
    list_display = ['owner', 'product', 'quantity']
