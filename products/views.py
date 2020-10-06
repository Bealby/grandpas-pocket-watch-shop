from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category


def all_products(request):
    # A view to return all products and search queries
    products = Product.objects.all()
    query = None
    categories = None

    if request.GET:
        # If Category exists
        if 'category' in request.GET:
            # Split into list by commas
            categories = request.GET['category'].split(',')
            # Filter categories in the list
            # Double underscore syntax allows for search in related model
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            # If query/ search is blank, message sent to inform user
            if not query:
                messages.error(request, "Please enter search criteria!")
                return redirect(reverse('products'))
            # Name or Description contains a query, which are case insensitive
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    # A view to display products independently
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
