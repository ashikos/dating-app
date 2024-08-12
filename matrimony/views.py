from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

def TestView(request):
    return render(request, 'index.html')

class HomeView(TemplateView):
    template_name = 'HOME/Home.html'

class ProfilesLocationView(TemplateView):
    template_name = 'HOME/Profiles_location.html'

class ProfilesDesignationView(TemplateView):
    template_name = 'HOME/Profiles_designation.html'

class ProfilesQualificationView(TemplateView):
    template_name = 'HOME/Profiles_qualification.html'

class SubscriptionPlanView(TemplateView):
    template_name = 'PAYMENT/Subscription_plan.html'

class PaymentMethodsView(TemplateView):
    template_name = 'PAYMENT/Payment_methods.html'

class AddPaymentMethodsView(TemplateView):
    template_name = 'PAYMENT/Add_payment_methods.html'
