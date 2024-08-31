from django.shortcuts import render
from . models import JobProfile

# Create your views here.

def TestView(request):
    return render(request, 'index.html')

def joblist(request):
    joblist = JobProfile.objects.all()
    
    return render(request, 'joblist.html',{'joblist':joblist})

def jobsingle1(request):
    return render(request, 'job-single-1.html')

def jobsingle2(request):
    return render(request, 'job-single-2.html')

def jobsingle3(request):
    return render(request, 'job-single-3.html')

def jobsingle4(request):
    return render(request, 'job-single-4.html')

def jobsingle5(request):
    return render(request, 'job-single-5.html')

def index8(request):
    return render(request, 'index/index-8.html')