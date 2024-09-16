from rest_framework import generics

from marketApp.models import Category, Subcategory, Product
from marketApp.paginators import MarketPaginator
from marketApp.serializers import CategorySerializer, SubcategorySerializer, SubcategoryViewSerializer, \
    CategoryViewSerializer, ProductSerializer, ProductViewSerializer


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


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductViewSerializer
    pagination_class = MarketPaginator


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductViewSerializer


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
