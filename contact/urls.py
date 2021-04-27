from django.urls import path
from .views import *

urlpatterns = [

    path('job-application', JobApplicate, name='job'),
    path('contact-us', ContactUs, name='contact_us'),

]