from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.contrib import messages
from service.models import Service

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
        return render(request, 'contact/job_applicat.html', {'services': services})


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
        return redirect('contact_us')
    else:
        return render(request, 'contact/contact_us.html', {})