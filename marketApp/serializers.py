from rest_framework import serializers

from marketApp.models import Category, Subcategory


class CategorySerializer(serializers.ModelSerializer):
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
