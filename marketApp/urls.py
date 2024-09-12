from django.urls import path

from marketApp.apps import MarketappConfig
from marketApp.views import CategoryCreateAPIView, CategoryListAPIView, CategoryUpdateAPIView, CategoryDestroyAPIView, \
    SubcategoryCreateAPIView, SubcategoryListAPIView

app_name = MarketappConfig.name

urlpatterns = [
    # Category
    path('category/create/', CategoryCreateAPIView.as_view(), name='category-create'),
    path('category/list/', CategoryListAPIView.as_view(), name='category-list'),
    path('category/update/<int:pk>/', CategoryUpdateAPIView.as_view(), name='category-update'),
    path('category/destroy/<int:pk>/', CategoryDestroyAPIView.as_view(), name='category-destroy'),

    # Subcategory
    path('subcategory/create/', SubcategoryCreateAPIView.as_view(), name='subcategory-create'),
    path('subcategory/list/', SubcategoryListAPIView.as_view(), name='subcategory-list'),
]
