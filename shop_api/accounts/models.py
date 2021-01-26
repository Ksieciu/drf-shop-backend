from django.conf import settings
from django.db import models


User = settings.AUTH_USER_MODEL


class ShippingDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    country = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    postcode = models.CharField(max_length=12)
    address = models.CharField(max_length=256)
    phone_number = models.IntegerField()