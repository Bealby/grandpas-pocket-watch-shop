from django.shortcuts import (
    render, redirect, HttpResponse, get_object_or_404
)

from django.http import HttpResponseRedirect
from django.contrib import messages

from products.models import Product


def view_basket(request):
    # A view to return the basket
    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    # Add product to shopping basket

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    # To ensure only one unique product is added to basket
    if item_id in list(basket.keys()):
        messages.warning(request, f'{product.name} is already in your basket')
    else:
        basket[item_id] = quantity
        messages.success(request, f'Added {product.name} to your basket')

    request.session['basket'] = basket
    # Redirect user to previous page
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove_from_basket(request, item_id):
    # Remove item from basket
    try:
        product = get_object_or_404(Product, pk=item_id)
        basket = request.session.get('basket', {})
        basket.pop(item_id)
        messages.success(request, f'Removed {product.name} from your basket')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
