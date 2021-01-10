import stripe
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import *
from django.core.mail import send_mail, EmailMessage
from django.http import HttpResponse
from service.models import Service, Employee, SpareParts, Request
from django.contrib import messages
from django.conf import settings
from .forms import RequestJobForm
from django.views.generic.edit import FormMixin
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# ! Home Page 

class HomeView(TemplateView):
    template_name = "home.html"


# ! Service

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

class EmployeeDetailView(LoginRequiredMixin, FormMixin, DetailView):
    model = Employee
    form_class = RequestJobForm
    login_url = "account_login"
    template_name = "service/employee_detail.html"

    def get_success_url(self):
        messages.add_message(self.request, messages.INFO,
                                  'تم إرسال طلبك إلى الموظف بنجاح وسوف يواصل معك خلال 15 دقيقة')
        return reverse('requests')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.employee = self.get_object()
        instance.save()
        return super(EmployeeDetailView, self).form_valid(form)


# ! Requests

@login_required(login_url='/account/login/')
def Requests(request):
    requests = Request.objects.filter(user=request.user).filter(show_in_history=True)
    return render(request, 'requests.html', {'requests': requests,})

@csrf_exempt
def UpdateStatus(request, pk):
    request = Request.objects.filter(pk=pk).update(status=True)
    return redirect('requests')

@csrf_exempt
def UpdateHistory(request, pk):
    request = Request.objects.filter(pk=pk).update(show_in_history=False)
    return redirect('requests')


# ! Spare Parts

class SparePartsTemplateView(LoginRequiredMixin, ListView):
    template_name = "spare_parts.html"
    model = SpareParts
    context_object_name = 'parts'
    login_url = "account_login"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY
        return context

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

def charge(request):
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=request.POST['data-amount'],
            currency='EGP',
            description=request.POST['data-description'],
            source=request.POST['stripeToken']
        )
    return render(request, 'spare_parts.html')


# ! Contacts 

def JobApplicate(request):
    services = Service.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        service = request.POST['service']
        about = request.POST['about']
        email = EmailMessage(
            'طلب عمل من ' + name,
            'الاسم : ' + name + '\n' +
            'رقم الهاتف : ' + phone + '\n' +
            'البريد الالكترونى : ' + email + '\n' +
            'الخدمة : ' + service +  '\n' +
            'نبذة عنى :' + about + '\n',
            email,
            ['omarelweshy@gmail.com', ],
        )
        email.send()
        messages.success(request, 'سيتم الرد عليك فى اقرب وقت ممكن.')
        return redirect('job')
    else:
        return render(request, 'job_applicat.html', {'services': services})


def ContactUs(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        reason = request.POST['reason']
        message = request.POST['message']
        email = EmailMessage(
            'رسالة من ' + name,
            'الاسم : ' + name + '\n' + 'البريد الالكترونى : ' + email + '\n'
            +'الموضوع :' + reason + '\n' + 'الرسالة : ' + message,
            email,
            ['omarelweshy@gmail.com', ],
        )
        email.send()
        messages.success(request, 'تم ارسال رسالتك للادارة وسيتم التواصل معك قريبا')
        return redirect('home')
    else:
        return render(request, 'contact_us.html', {})

