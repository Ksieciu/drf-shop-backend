from rest_framework import serializers
from .models import Product, Category

AVAILABILITY_STATUS = [
        ('IN', 'In Stock'),
        ('OUT', 'Out of stock'),
        ('SOON', 'Available soon'),
    ]


class CategorySerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Category
        fields = [
            "category_name",
            "products_count"
            ]

    def get_products_count(self, obj):
        return obj.count_products_in_category()


class ProductSerializer(serializers.ModelSerializer):
    availability = serializers.ChoiceField(choices=AVAILABILITY_STATUS)
    category = serializers.SlugRelatedField(
        slug_field='category_name',
        queryset=Category.objects.all(), 
        required=False, 
        many=True)

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
        ]


class ShowProductSerializer(ProductSerializer):
    availability = serializers.CharField(source='get_availability_display')
    category = CategorySerializer(required=False, many=True, read_only=True)





