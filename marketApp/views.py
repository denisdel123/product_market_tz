from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from marketApp.models import Category, Subcategory, Product, CartView
from marketApp.paginators import MarketPaginator
from marketApp.serializers import CategorySerializer, SubcategorySerializer, SubcategoryViewSerializer, \
    CategoryViewSerializer, ProductSerializer, ProductViewSerializer, CartViewSerializer, CartViewListSerializer


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
    permission_classes = [IsAuthenticated]


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductViewSerializer


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()


class CartViewCreateAPIView(generics.CreateAPIView):
    serializer_class = CartViewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CartView.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        product = serializer.validated_data['product']
        quantity = serializer.validated_data['quantity']

        cart_view, item_product = CartView.objects.get_or_create(owner=self.request.user, product=product)

        if not item_product:
            cart_view.quantity += quantity
        else:
            cart_view.quantity = quantity

        cart_view.save()


class CartViewListAPIView(generics.ListAPIView):
    serializer_class = CartViewListSerializer
    pagination_class = MarketPaginator
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CartView.objects.filter(owner=self.request.user.pk)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        # Подсчитываем общее количество и общую стоимость
        total_items = len(serializer.data)
        total_price = sum(item.quantity * item.product.price for item in queryset)

        # Формируем ответ
        response_data = {
            'items': serializer.data,  # Данные корзины
            'total_items': total_items,  # Общее количество товаров
            'total_price': total_price  # Общая стоимость товаров
        }

        return Response(response_data)


class CartViewDestroyAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CartView.objects.filter(owner=self.request.user)

    def get_object(self):
        product_id = self.kwargs['pk']
        return get_object_or_404(CartView, owner=self.request.user, product_id=product_id)

    def perform_destroy(self, instance):
        if instance.quantity > 1:
            instance.quantity -= 1
            instance.save()
            return Response({
                "message": "Количество товара уменьшено на 1.",
                "quantity": instance.quantity
            }, status=status.HTTP_200_OK)

        else:
            instance.delete()
            return Response({"message": "Товар удалён из корзины."}, status=status.HTTP_204_NO_CONTENT)


class CartViewAllDestroyAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CartView.objects.filter(owner=self.request.user)

    def delete(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        queryset.delete()
        return Response({'massage': 'Корзина очищена'}, status=status.HTTP_204_NO_CONTENT)
