from rest_framework import serializers

from marketApp.models import Category, Subcategory, Product, CartView


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ['slug']


class CategoryViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        exclude = ['slug']


class SubcategoryViewSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()

    class Meta:
        model = Subcategory
        fields = '__all__'

    def get_category(self, obj):
        return obj.associated_category.name


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['slug']


class ProductViewSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    subcategory = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_category(self, obj):
        return obj.associated_subcategory.associated_category.name

    def get_subcategory(self, obj):
        return obj.associated_subcategory.name


class CartViewSerializer(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source='product')

    class Meta:
        model = CartView
        fields = ['product_id', 'quantity']


class CartViewListSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = CartView
        fields = '__all__'

    def get_total_price(self, obj):
        return obj.quantity * obj.product.price
