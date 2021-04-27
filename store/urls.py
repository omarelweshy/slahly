from django.urls import path

from .views import SparePartsTemplateView as SparePartsView


urlpatterns = [
    path('store', SparePartsView.as_view(), name='store'),
]