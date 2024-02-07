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
        'stripe_public_key': 'pk_test_51OdyQhDyRuX5ADdDCL6cnhUWQByFjbmtnx82jOIPi71865qLawuUB1NBWjtbgSGRPm7r5vGc2QmAj0INeRnL3lxi00syeIaA8W',
        'client_secret': 'sk_test_51OdyQhDyRuX5ADdD24QX1gpyYqCEl48kdi6ZHsvxyK2rnZZoDn7z0Rj2yPBlUUcUsNXJ1oYHgxLaFSsgTAxggJI800H2DeAIQ8'
    }

    return render(request, template, context)