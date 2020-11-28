from django.shortcuts import render
from django.views.generic import *

class HomeView(TemplateView):
    template_name = "blank.html"

class ServiceView(TemplateView):
    template_name = "service.html"