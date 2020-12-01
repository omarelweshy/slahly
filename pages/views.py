from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import *
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from service.models import Service, Employee

class HomeView(TemplateView):
    template_name = "home.html"

class ServiceListView(ListView):
    model = Service
    context_object_name = 'services'
    template_name = "service.html"

def Employees(request, pk):
    service = get_object_or_404(Service, pk=pk)
    employees = Employee.objects.all()
    context = {
        'service': service,
        'employees': employees
    }
    return render(request, 'employees.html', context)


def JobApplicate(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        about = request.POST['about']
        
        send_mail(
            'طلب عمل من ' + name,
            'نبذة عنى :' + about + '\n' + 'رقم الهاتف : ' + phone + '\n' + 'البريد الالكترونى : ' + email,
            email,
            ['omarelweshy@gmail.com',],
        )
        return HttpResponse('Done!')
    else:
        return render(request, 'job_applicat.html', {})






    #          return redirect('success')