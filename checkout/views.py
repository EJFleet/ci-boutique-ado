from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51QhFQpF7OeopN5TT78Z0YDwPXoYp6D54l2h6Rx7sbCQbLCZL5tQ40fiRWNsHHGNs6N2mz77ut1fTEjHuLlth4Qw600USMDc4yw',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
