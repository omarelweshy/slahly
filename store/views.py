import stripe
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *
from django.conf import settings
from store.models import SpareParts

# Create your views here.
class SparePartsTemplateView(LoginRequiredMixin, ListView):
    template_name = "spare_parts.html"
    model = SpareParts
    context_object_name = 'parts'
    login_url = "account_login"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY
        return context

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

def charge(request):
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=request.POST['data-amount'],
            currency='EGP',
            description=request.POST['data-description'],
            source=request.POST['stripeToken']
        )
    return render(request, 'spare_parts.html')