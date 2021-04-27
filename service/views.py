from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from service.models import Service, Employee

# Create your views here.
class ServiceListView(ListView):
    model = Service
    context_object_name = 'services'
    template_name = "service/service.html"

@login_required(login_url='/account/login/')
def ServiceEmployeesList(request, pk):
    service = get_object_or_404(Service, pk=pk)
    employees = Employee.objects.all()
    context = {
        'service': service,
        'employees': employees
    }
    return render(request, 'service/employees.html', context)