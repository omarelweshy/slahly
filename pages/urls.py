from django.urls import path
from .views import *




urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('service', ServiceListView.as_view(), name='service'),
    path('service/<int:pk>', Employees, name='employees'),
    path('job-application', JobApplicate, name='job'),
]
