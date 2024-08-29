from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class SigninView(TemplateView):
    template_name = 'Register/temp/login.html'

class SignupView(TemplateView):
    template_name = 'Register/temp/register.html'

def TestView(request):
    return render(request, 'Register/temp/login.html')

def accept_view(request):
    return render(request, 'accept.html')

def contacted_view(request):
    return render(request, 'contacted.html')

def extra_view(request):
    return render(request, 'extra.html')

def messages_view(request):
    return render(request, 'messages.html')

def received_view(request):
    return render(request, 'received.html')

def reject_view(request):
    return render(request, 'reject.html')

def sent_view(request):
    return render(request, 'sent.html')

def shortlist_view(request):
    return render(request, 'shortlist.html')

def shortlisted_view(request):
    return render(request, 'shortlisted.html')

def shortlistedby_view(request):
    return render(request, 'shortlistedby.html')

def viewedmyprofile_view(request):
    return render(request, 'viewedmyprofile.html')

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
    



class ProfileDescription(TemplateView):
    template_name = 'TARGETUSER/profile_description.html'
    
class UserProfileView(TemplateView):
    template_name = 'USERPROFILE/profile.html'
      
class EditProfile(TemplateView):
    template_name = 'USERPROFILE/edit_profile.html'
    
class ChangePasswordView(TemplateView):
    template_name = 'USERPROFILE/change_password.html'
    
class SettingsView(TemplateView):
    template_name = 'USERPROFILE/settings.html'
    
class PrivacySettingsView(TemplateView):
    template_name = 'USERPROFILE/privacy.html'
    
class PartnerView(TemplateView):
    template_name = 'USERPROFILE/partner_preference.html'

