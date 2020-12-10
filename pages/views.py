from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import *
from django.core.mail import send_mail, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from service.models import Service, Employee, SpareParts, Request
from django.contrib import messages
from django.conf import settings
import stripe
from .forms import RequestJobForm
from django.views.generic.edit import FormMixin, ModelFormMixin
from django.urls import reverse

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


def JobApplicate(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        about = request.POST['about']
        email = EmailMessage(
            'طلب عمل من ' + name,
            'الاسم : ' + name + '\n' 'نبذة عنى :' + about + '\n' +
            'رقم الهاتف : ' + phone + '\n' + 'البريد الالكترونى : ' + email,
            email,
            ['omarelweshy@gmail.com', ],
        )
        email.send()
        messages.success(request, 'سيتم الرد عليك فى اقرب وقت ممكن.')
        return redirect('job')
    else:
        return render(request, 'job_applicat.html', {})

def Requests(request):
    requests = Request.objects.all()
    return render(request, 'requests.html', {'requests': requests})

class EmployeeDetailView(FormMixin, DetailView):
    model = Employee
    form_class = RequestJobForm
    template_name = "employee_detail.html"

    def get_success_url(self):
         if True:
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

