from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models
from stock.models import Product


User = settings.AUTH_USER_MODEL


# it might be better to keep cart in cached db, 
# but for this project I'll stick with this approach
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(
        max_length=256, 
        blank=True, 
        default="Cart")
    saved = models.BooleanField(blank=True, default=False)
    slug = models.SlugField(blank=True, null=True)
    products = models.ManyToManyField(
        Product, 
        through="CartProduct", 
        related_name="cart_products")

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.user.username + self.name
        super().save(*args, **kwargs)

    def get_total_price(self):
        total = 0
        for product in self.products.all():
            total += product.get_total_product_price()
        return total

    def get_products_number(self):
        return self.products.all().count()


class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(
        validators=[MinValueValidator(0)],
        default=1)

    def __str__(self):
        return self.product.product_name + ' - ' + self.cart.slug

    def save(self, *args, **kwargs):
        self.total_product_price = self.get_total_product_price()
        super().save(*args, **kwargs)

    def get_total_product_price(self):
        return self.quantity * self.product.price
