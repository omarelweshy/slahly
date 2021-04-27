from django.urls import path
from .views import Requests, UpdateHistory, UpdateStatus


urlpatterns = [

    # ! Requests 
    path('', Requests, name='requests'),
    path('UpdateStatus/<int:pk>', UpdateStatus, name='UpdateStatus'),
    path('UpdateHistory/<int:pk>', UpdateHistory, name='UpdateHistory'),

]