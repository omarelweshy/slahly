from django.urls import path
from .views import EmplyeeDetail

urlpatterns = [
    path('<int:pk>', EmplyeeDetail, name='employee_detail'),
]