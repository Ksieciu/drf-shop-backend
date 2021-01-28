from django.db import models
from django.core.validators import MinValueValidator
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify


class Product(models.Model):
    AVAILABILITY_STATUS = [
        ('IN', 'In Stock'),
        ('OUT', 'Out of stock'),
        ('SOON', 'Available soon'),
    ]
    product_name = models.CharField(max_length=256, unique=True)
    category = models.ManyToManyField('Category')
    price = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        validators=[MinValueValidator(0)])
    promotion_price = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        blank=True,
        null=True)
    promotion_going = models.BooleanField(default=False)
    description = models.TextField(
        max_length=1024, 
        null=True, 
        blank=True)
    stock = models.IntegerField(
        validators=[MinValueValidator(0)], 
        default=0, 
        blank=True)
    availability = models.CharField(
        max_length=4, 
        choices=AVAILABILITY_STATUS,
        default='OUT',
        blank=True)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return f'{self.product_name}: {self.price}, Stock: {self.stock}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.product_name)
        if self.stock == 0 and self.availability == 'IN':
            self.availability = 'OUT'
        super().save(*args, **kwargs)


class Category(models.Model):
    category_name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return f'{self.category_name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category_name)
        super().save(*args, **kwargs)

    def count_products_in_category(self):
        return Product.objects.filter(category=self.id).count()



@receiver(pre_save, sender=Product)
def on_create(sender, instance: Product, **kwargs):
    '''
    Checks if it's on creation save and then 
    sets avaiability for "in stock" if stock
    is bigger than 0
    '''
    if not Product.objects.filter(id=instance.id).exists():
        if instance.stock > 0:
            instance.availability = 'IN'