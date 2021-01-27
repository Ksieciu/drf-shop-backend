from rest_framework import serializers
from .models import CartProduct, Cart
from stock.serializers import ProductSerializer
from stock.models import Product


class CartProductSerializer(ProductSerializer):
    total_product_price = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "product_name",
            "category",
            "price",
            "promotion_price",
            "promotion_going",
            "description",
            "stock",
            "availability",
            "total_product_price",
        ]

    def get_total_product_price(self, obj):
        cart_id = self.context.get("cart_id")
        cart_product = CartProduct.objects.get(cart=cart_id, product=obj.id)
        total_price = cart_product.get_total_product_price()
        return total_price



class CartSerializer(serializers.ModelSerializer):
    user = serializers.CurrentUserDefault()
    products = CartProductSerializer(many=True, required=False)

    class Meta:
        model = Cart
        fields = [
            "user",
            "products",
        ]