from django.shortcuts import render, redirect
from request.models import Request
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

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