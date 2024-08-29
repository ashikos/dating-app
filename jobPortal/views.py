from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request,'pages/home.html')


def login(request):
    return render(request,'registration/login.html')
def user_register(request):
    return render(request,'registration/register.html')
    
def job_details(request):
    return render(request,'Job/job_detail.html')

def contact (request):
    return render(request,'pages/contact.html')

def about (request):
    return render(request,'pages/about.html') 
