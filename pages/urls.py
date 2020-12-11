from django.urls import path
from .views import *




urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('service', ServiceListView.as_view(), name='service'),
    path('service/<int:pk>', ServiceEmployeesList, name='employees'),
    path('employee/<int:pk>', EmployeeDetailView.as_view(), name='employee_detail'),
    path('job-application', JobApplicate, name='job'),
    path('store', SparePartsTemplateView.as_view(), name='store'),
    # path('requests', RequestsListView.as_view(), name='requests'),
    path('requests', Requests, name='requests'),
    # path('charge', charge, name='charge'),
    path('UpdateStatus/<int:pk>', UpdateStatus, name='UpdateStatus'),
    path('UpdateHistory/<int:pk>', UpdateHistory, name='UpdateHistory'),
]
