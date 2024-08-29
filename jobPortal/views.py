from django.shortcuts import render


# Create your views here.


def EmployeeDashbaord(request):
    return render(request, 'JobPortal/EmployerDashboard/dashboard.html')
