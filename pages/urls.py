from django.urls import path
from .views import *




urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('service', ServiceListView.as_view(), name='service'),
    path('service/<int:pk>', Employees, name='employees'),
    path('employee/<int:pk>', EmployeeDetail, name='employee_detail'),
    path('job-application', JobApplicate, name='job'),
    path('store', SparePartsTemplateView.as_view(), name='store'),
    # path('charge', charge, name='charge'),
]
