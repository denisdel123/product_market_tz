from rest_framework import generics

from marketApp.models import Category, Subcategory
from marketApp.paginators import MarketPaginator
from marketApp.serializers import CategorySerializer, SubcategorySerializer, SubcategoryViewSerializer, \
    CategoryViewSerializer


# Эндпоинты Категорий
class CategoryCreateAPIView(generics.CreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryViewSerializer
    pagination_class = MarketPaginator


class CategoryUpdateAPIView(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDestroyAPIView(generics.DestroyAPIView):
    queryset = Category.objects.all()


# Эндпоинты подкатегорий
class SubcategoryCreateAPIView(generics.CreateAPIView):
    queryset = Subcategory
    serializer_class = SubcategorySerializer


class SubcategoryListAPIView(generics.ListAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategoryViewSerializer
    pagination_class = MarketPaginator


class SubcategoryUpdateAPIView(generics.UpdateAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer


class SubcategoryDestroyAPIView(generics.DestroyAPIView):
    queryset = Subcategory.objects.all()
