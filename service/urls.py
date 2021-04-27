from django.urls import path
from .views import ServiceListView, ServiceEmployeesList


urlpatterns = [
    path('', ServiceListView.as_view(), name='service'),
    path('<int:pk>', ServiceEmployeesList, name='employees'),
]