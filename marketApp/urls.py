from django.urls import path

from marketApp.apps import MarketappConfig
from marketApp.views import CategoryCreateAPIView, CategoryListAPIView, CategoryUpdateAPIView, CategoryDestroyAPIView, \
    SubcategoryCreateAPIView, SubcategoryListAPIView, SubcategoryUpdateAPIView, SubcategoryDestroyAPIView, \
    ProductCreateAPIView, ProductListAPIView, ProductRetrieveAPIView, ProductUpdateAPIView, ProductDestroyAPIView, \
    CartViewCreateAPIView, CartViewListAPIView, CartViewDestroyAPIView

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
    path('subcategory/update/<int:pk>/', SubcategoryUpdateAPIView.as_view(), name='subcategory-update'),
    path('subcategory/destroy/<int:pk>/', SubcategoryDestroyAPIView.as_view(), name='subcategory-destroy'),

    # Product
    path('product/create/', ProductCreateAPIView.as_view(), name='product-create'),
    path('product/list/', ProductListAPIView.as_view(), name='product-list'),
    path('product/retrieve/<int:pk>/', ProductRetrieveAPIView.as_view(), name='product-retrieve'),
    path('product/update/<int:pk>/', ProductUpdateAPIView.as_view(), name='product-update'),
    path('product/destroy/<int:pk>/', ProductDestroyAPIView.as_view(), name='product-destroy'),

    # cartView
    path('cart-view/create/', CartViewCreateAPIView.as_view(), name='cart-view-create'),
    path('cart-view/list/', CartViewListAPIView.as_view(), name='cart-view-list'),
    path('cart-view/destroy/<int:pk>/', CartViewDestroyAPIView.as_view(), name='cart-view-destroy'),
]
