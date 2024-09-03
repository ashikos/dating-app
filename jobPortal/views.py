from django.shortcuts import render
from . models import JobProfile
from django.shortcuts import render, get_object_or_404

# Create your views here.

def TestView(request):
    return render(request, 'index.html')

def joblist(request):
    joblist = JobProfile.objects.all()
    return render(request, 'joblist.html',{'joblist':joblist})

def job_detail(request, pk):
    job = get_object_or_404(JobProfile, pk=pk)  # Fetch the job profile by primary key
    return render(request, 'job_detail.html', {'job': job}) 

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