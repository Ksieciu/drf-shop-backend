import datetime
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from products.models import Product
from shipping_details.models import ShippingDetails

User = settings.AUTH_USER_MODEL

ORDER_PLACED = 'PLACED'
IN_REALIZATION = 'REALIZATION'
SENT = 'SENT'
CANCELLED = 'CANCELLED'
COMPLETED = 'COMPLETED'
ORDER_STATUS = [
    (ORDER_PLACED, 'Order placed'),
    (IN_REALIZATION, 'In realization'),
    (SENT, 'Order sent'),
    (CANCELLED, 'Cancelled'),
    (COMPLETED, 'Completed'),
]

CASH = 'CASH'
CREDIT_CARD = 'CREDIT'
BANK_TRANSFER = 'TRANSFER'
PAYMENT_TYPE = [
    (CASH, 'Cash'),
    (CREDIT_CARD, 'Credit Card'),
    (BANK_TRANSFER, 'Bank Transfer'),
]


class Order(models.Model):
    user = models.ForeignKey(User)
    shipping_details = models.ForeignKey(ShippingDetails)
    status = models.CharField(
        max_length=11, 
        choices=AVAILABILORDER_STATUSITY_STATUS, 
        default='PLACED')
    payment_type = CharField(
        max_length=8, 
        choices=PAYMENT_TYPE, 
        default='CASH')
    payment_complete = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now_add=True)
    send_date = models.DateTimeField(blank=True, null=True)
    completed_date = models.DateTimeField(blank=True, null=True)
    cancellation_date = models.DateTimeField(blank=True, null=True)


class Cart(models.Model):
    user = models.ForeignKey(User)
    products = models.ManyToManyField(
        Product, 
        through="CartProduct", 
        related_name="cart_products")

    def get_total_price(self):
        total = 0
        for product in self.products.all():
            total += product.get_total_product_price()
        return total


class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def get_total_product_price(self):
        return self.quantity * self.product.price



@receiver(pre_save, sender=Order)
def on_change(sender, instance: Order, **kwargs):
    '''
    Automatically change send, cancelled 
    and completed dates when status changes
    (change for status change date if date
    was not specified in save())
    '''
    prev_order = Order.objects.get(id=instance.id)
    if prev_order.status != instance.status:
        if instance.status == 'SENT' and prev_order.send_date == instance.send_date:
            instance.send_date = datetime.datetime.now()
        if instance.status == 'CANCELLED' and prev_order.cancellation_date == instance.cancellation_date:
            instance.cancellation_date = datetime.datetime.now()
        if instance.status == 'COMPLETED' and prev_order.completed_date == instance.completed_date:
            instance.completed_date = datetime.datetime.now()