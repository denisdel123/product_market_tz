from rest_framework import generics

from marketApp.models import Category, Subcategory
from marketApp.paginators import MarketPaginator
from marketApp.serializers import CategorySerializer, SubcategorySerializer, SubcategoryViewSerializer


class CategoryCreateAPIView(generics.CreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = MarketPaginator


class CategoryUpdateAPIView(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDestroyAPIView(generics.DestroyAPIView):
    queryset = Category.objects.all()


class SubcategoryCreateAPIView(generics.CreateAPIView):
    queryset = Subcategory
    serializer_class = SubcategorySerializer


class SubcategoryListAPIView(generics.ListAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategoryViewSerializer
