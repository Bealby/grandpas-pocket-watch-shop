from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)
    

class OrderLineItemAdminInline(admin.TabularInline):
    inlines = (OrderLineItemAdminInline,)

    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)
    # Read only to prevent fraud/editing reducing integrity of order
    readonly_fields = ('order_number', 'date', 'delivery_cost', 'order_total', 'grand_total')
    # Fixes order of fields 
    fields = ('order_number', 'date', 'full_name', 'email', 'phone_number', 'country', 'postcode', 'town_or_city', 'street_address1', 'street_address2', 'county', 'delivery_cost', 'order_total', 'grand_total')
    # Restrict columns that show up in the order list to selective few.
    list_display = ('order_number', 'date', 'full_name', 'order_total', 'delivery_cost', 'grand_total')


    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)