from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import *
from django.core.mail import send_mail, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from service.models import Service, Employee, SpareParts
from django.contrib import messages
from django.conf import settings
import stripe


stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

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

def EmployeeDetail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'employee_detail.html', {'employee': employee})

def JobApplicate(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        about = request.POST['about']
        email = EmailMessage(
            'طلب عمل من ' + name,
            'الاسم : ' +  name + '\n' 'نبذة عنى :' + about + '\n' + 'رقم الهاتف : ' + phone + '\n' + 'البريد الالكترونى : ' + email,
            email,
            ['omarelweshy@gmail.com',],
        )
        email.send()
        messages.success(request, 'سيتم الرد عليك فى اقرب وقت ممكن.')
        return redirect('job')
    else:
        return render(request, 'job_applicat.html', {})


class SparePartsTemplateView(ListView):
    template_name = "spare_parts.html"
    model = SpareParts
    context_object_name = 'parts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY
        return context

def charge(request):
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=request.POST['data-amount'],
            currency='EGP',
            description=request.POST['data-description'],
            source=request.POST['stripeToken']
        )
    return render(request, 'spare_parts.html')