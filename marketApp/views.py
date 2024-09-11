from rest_framework import generics

from marketApp.models import Category
from marketApp.serializers import CategorySerializer


class CategoryCreateAPIView(generics.CreateAPIView):
    serializer_class = CategorySerializer


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

