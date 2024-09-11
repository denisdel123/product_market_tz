from django.urls import path

from marketApp.apps import MarketappConfig
from marketApp.views import CategoryCreateAPIView, CategoryListAPIView, CategoryUpdateAPIView, CategoryDestroyAPIView

app_name = MarketappConfig.name

urlpatterns = [
    path('category/create/', CategoryCreateAPIView.as_view(), name='category-create'),
    path('category/list/', CategoryListAPIView.as_view(), name='category-list'),
    path('category/update/<int:pk>/', CategoryUpdateAPIView.as_view(), name='category-update'),
    path('category/destroy/<int:pk>/', CategoryDestroyAPIView.as_view(), name='category-destroy'),
]