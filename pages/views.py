from django.shortcuts import render
from django.views.generic import *
from service.models import Service

class HomeView(TemplateView):
    template_name = "home.html"

class ServiceView(ListView):
    model = Service
    template_name = "service.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["service"] = Service.objects.all()
        return context
    