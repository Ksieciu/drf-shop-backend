from rest_framework import serializers
from .models import CartProduct, Cart
from stock.serializers import ProductSerializer
from stock.models import Product


class CartAddProductSerializer(serializers.Serializer):
    '''
    This serializer is strictly for adding item to default
    cart, as we assume that we only can work on default cart.
    If we want to work on saved card, then we need to load it
    first into default cart.
    '''
    user = serializers.SerializerMethodField('_user')
    product_id = serializers.PrimaryKeyRelatedField(read_only=True)

    def _user(self):
        request = self.context.get('request', None)
        if request:
            return request.user

    def create(self, validated_data):
        user = validated_data['user']
        if user is not None:
            cart, created = Cart.objects.get_or_create(
                user=user,
                slug=user.username
            )
            cart_product, created = CartProduct.objects.get_or_create(
                user=user,
                product_id=validated_data['product_id']
            )


class CartRemoveProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProduct
        fields = ["id"]


class CartProductAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProduct
        fields = [""]


class CartProductSerializer(ProductSerializer):
    """
    Serializes informations about products in cart
    with additional function showing full price of
    given product(quantity * price)
    """
    total_product_price = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "id",
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
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    products = CartProductSerializer(many=True, required=False)

    class Meta:
        model = Cart
        fields = [
            "user",
            "name",
            "products",
        ]