from rest_framework import serializers

from marketApp.models import Category, Subcategory, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ['slug']


class CategoryViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        exclude = ['slug']


class SubcategoryViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['slug']


class ProductViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
