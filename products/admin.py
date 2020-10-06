from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    # Displayed fields in Admin
    list_display = (
        'sku',
        'name',
        'category',
        'image',
    )

    # Orders by latest sku
    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
