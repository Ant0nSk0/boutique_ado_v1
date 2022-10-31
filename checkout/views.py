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
        'stripe_public_key': 'pk_test_51Lz7YFAzDjF2D7TUWbBFu50TyYjfZ1F4r8UxMTO9dQpD6h46eLCnLHkaxzSOrKPL0MQkB4hxOqCsAs26OXaVil0Z00LB7Yd89v',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)