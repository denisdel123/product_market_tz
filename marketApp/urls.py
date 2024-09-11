from django.urls import path

from marketApp.apps import MarketappConfig
from marketApp.views import CategoryCreateAPIView, CategoryListAPIView

app_name = MarketappConfig.name

urlpatterns = [
    path('category/create/', CategoryCreateAPIView.as_view(), name='category-create'),
    path('category/list/', CategoryListAPIView.as_view(), name='category-list'),
]