from django.shortcuts import render
from .models import Product

# Create your views here.

def index(request):
    # A view to return all products and search queries

    products = Product.objects.all
    
    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)