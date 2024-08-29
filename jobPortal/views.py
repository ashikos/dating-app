from django.shortcuts import render


# Create your views here.

# ###############BASIC PAGE##################
def home(request):
    return render(request,'pages/home.html')
def contact (request):
    return render(request,'pages/contact.html')

def about (request):
    return render(request,'pages/about.html') 

# ##################END######################



# ##################USER MODULE#######################


def login(request):
    return render(request,'registration/login.html')
def user_register(request):
    return render(request,'registration/register.html')

def logout(request):
    pass
#######################END###########################

# ##################JOBSEEKER MODULE#######################


#######################END###########################


# ##################EMPLOYER MODULE#######################
    
def job_details(request):
    return render(request,'Job/job_detail.html')

def job_create(request):
    return render(request,'Job/job_create.html')


def job_update(request):
    return render(request,'Job/job_update.html')

def job_delete(request):
    return render(request,'Job/job_delete.html')
#######################END###########################