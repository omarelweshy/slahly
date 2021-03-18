from django.urls import path
# from django.conf.urls import (
# handler400, handler403, handler404, handler500
# )
from .views import *

urlpatterns = [
    # ! Home 
    path('', HomeView.as_view(), name='home'),

    # ! Service
    path('service', ServiceListView.as_view(), name='service'),
    path('service/<int:pk>', ServiceEmployeesList, name='employees'),
    path('employee/<int:pk>', EmployeeDetailView.as_view(), name='employee_detail'),

    # ! Requests 
    path('requests', Requests, name='requests'),
    path('UpdateStatus/<int:pk>', UpdateStatus, name='UpdateStatus'),
    path('UpdateHistory/<int:pk>', UpdateHistory, name='UpdateHistory'),

    # ! Spare Parts
    path('store', SparePartsTemplateView.as_view(), name='store'),
    # path('charge', charge, name='charge'),

    # ! Contacts
    path('job-application', JobApplicate, name='job'),
    path('contact-us', ContactUs, name='contact_us'),
]

# handler404 = 'pages.views.handler404'
