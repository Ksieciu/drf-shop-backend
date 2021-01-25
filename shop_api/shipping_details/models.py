from django.conf import settings
from django.db import models


User = settings.AUTH_USER_MODEL


class ShippingDetails(models.Models):
    user = models.ForeignKey(User)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    country = models.CharField(max_length=128, default="Poland")
    city = models.CharField(max_length=128)
    postcode = models.CharField(max_length=12)
    address = models.CharField(max_length=256)
    phone_number = models.IntegerField(max_length=12)
