from django.shortcuts import render, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    basket = request.session.get('basket', {})
    # To prevent people from manually accessing the URL by typing /checkout
    if not basket:
        message.error(request, "there's nothing in your basket at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    } 

    return render(request, template, context)

