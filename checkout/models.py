import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from products.models import Product


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=false, editable=False)
    full_name = models.CharField(max_length=50, null=false, black=False)
    email = models.CharField(max_length=254, null=false, black=False)
    phone_number_number = models.CharField(max_length=20, null=false, black=False)
    county = models.CharField(max_length=40, null=false, black=False)
    # Postcode not required as do not exist in every country
    postcode = models.CharField(max_length=20, null=false, black=False)
    town_or_city = models.CharField(max_length=40, null=false, black=False)
    street_address1 = models.CharField(max_length=80, null=false, black=False)
    street_address2 = models.CharField(max_length=80, null=false, black=False)
    # County not required as do not exist in every country
    county = models.CharField(max_length=80, null=false, black=False)
    date = models.CharField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_length=6, decimal_places=2, null=False default=0)
    order_total = models.DecimalField(max_length=10, decimal_places=2, null=False default=0)
    grand_total = models.DecimalField(max_length=10, decimal_places=2, null=False default=0)

    def _generate_order_number(self):
    # Generate unique order number using UUID
        return uuid.uuid4().hex.upper()

class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

