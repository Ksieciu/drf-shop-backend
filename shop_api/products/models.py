from django.db import models


class Product(models.Model):
    IN_STOCK = 'IN'
    OUT_OF_STOCK = 'OUT'
    AVAILABLE_SOON = 'SOON'
    AVAILABILITY_STATUS = [
        (IN_STOCK, 'In Stock'),
        (OUT_OF_STOCK, 'Out of stock'),
        (AVAILABLE_SOON, 'Available soon'),
    ]
    product_name = models.CharField(max_length=256)
    category = models.ManyToManyField('Category')
    price = models.DecimalField(min=0)
    promotion_price = models.DecimalField(min=0)
    promotion_going = models.BooleanField(default=False)
    description = models.TextField(max_length=1024, null=True, blank=True)
    stock = models.IntegerField(min=0, default=0)
    availability = models.Choices(max_length=4, choices=AVAILABILITY_STATUS)

    def __str__(self):
        return f'{self.product_name}: {self.product_price}, Stock: {stock}'

    def save(self, *args, **kwargs):
        if self.stock = 0 and self.availability == 'IN':
            self.availability = 'OUT'
        super().save(*args, **kwargs)


class Category(models.Model):
    category_name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return f'{self.category_name}'

    def count_products_in_category(self):
        return Product.objects.filter(category=self.id).count()