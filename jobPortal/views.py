from django.shortcuts import render


# Create your views here.

def TestView(request):
    return render(request, 'JobPortal/EmployerDashboard/dashboard.html')
