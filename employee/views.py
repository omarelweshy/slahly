from django.shortcuts import render
from django.http import HttpResponseRedirect
from employee.forms import RequestJobForm, AddCommentForm
from service.models import Employee
from django.contrib import messages
from django.shortcuts import render, redirect

def EmplyeeDetail(request, pk):
    employee = Employee.objects.get(pk=pk)
    jobRequest = RequestJobForm(request.POST or None, prefix='job_request')
    comment = AddCommentForm(request.POST or None, prefix='comment')

    if request.method == 'POST':
        if jobRequest.is_valid():
            instance = jobRequest.save(commit=False)
            instance.user = request.user
            instance.employee = employee
            instance.save()
            messages.success(request, 'تم إرسال طلبك إلى الموظف بنجاح وسوف يواصل معك خلال 15 دقيقة')
            return redirect('requests')

        elif comment.is_valid():
            instance = comment.save(commit=False)
            instance.user = request.user
            instance.employee = employee
            instance.save()
            return HttpResponseRedirect(request.path_info)
        else:
            jobRequest = RequestJobForm()
            comment = AddCommentForm()

    context = {
        'employee': employee,
        'jobRequest_form': jobRequest,
        'comment_form': comment,
    }
    return render(request, 'service/employee_detail.html', context)