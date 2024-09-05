from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .forms import UserProfileForm, PartnerExpectationsForm
from .models import UserProfile, PartnerExpectations
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import get_user_model
User = get_user_model()
from django.views import View
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required

# Create your views here.
class SigninView(TemplateView):
    template_name = 'Register/temp/login.html'

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)  # Use username for authentication
        if user is not None:
            login(request, user)
            return redirect(reverse('extra'))
        else:
            messages.error(request, 'Invalid email or password')
            return render(request, self.template_name, {
                'email': email,
                'password': password
            })

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    

class SignupView(View):
    template_name = 'Register/temp/register.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirmPassword']

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return render(request, self.template_name)

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already in use.')
            return render(request, self.template_name)

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=email,  # Assuming the username is the email
            password=make_password(password)
        )
        user.save()
        messages.success(request, 'Registration successful. Please log in.')
        return redirect(reverse('login'))

def TestView(request):
    return render(request, 'Register/temp/login.html')

def accept_view(request):
    return render(request, 'accept.html')

def contacted_view(request):
    return render(request, 'contacted.html')


# @login_required
# def extra_view(request):
#     user = request.user  # Fetch the logged-in user
#     user_profile = get_object_or_404(UserProfile, user=user)  # Fetch the user's profile
#     partner_expectations = PartnerExpectations.objects.filter(user_profile=user_profile).first()

#     if request.method == 'POST':
#         if 'save_profile' in request.POST:
#             profile_form = UserProfileForm(request.POST, instance=user_profile)
#             if profile_form.is_valid():
#                 profile_form.save()
#                 return redirect('extra')  # Redirect after saving
#         elif 'save_expectations' in request.POST:
#             expectations_form = PartnerExpectationsForm(request.POST, instance=partner_expectations)
#             if expectations_form.is_valid():
#                 expectations_form.save()
#                 return redirect('extra')  # Redirect after saving
#     else:
#         profile_form = UserProfileForm(instance=user_profile)
#         expectations_form = PartnerExpectationsForm(instance=partner_expectations)

#     return render(request, 'extra.html', {
#         'profile_form': profile_form,
#         'expectations_form': expectations_form,
#     })
@login_required
def extra_view(request):
    # Get or create the user profile of the logged-in user
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    # Get the first partner expectation related to this user profile or None
    partner_expectations = PartnerExpectations.objects.filter(user_profile=user_profile).first()

    if request.method == 'POST':
        if 'save_profile' in request.POST:
            profile_form = UserProfileForm(request.POST, instance=user_profile)
            if profile_form.is_valid():
                profile_form.save()
                return redirect('home')  # Redirect after saving the profile
        elif 'save_expectations' in request.POST:
            expectations_form = PartnerExpectationsForm(request.POST, instance=partner_expectations)
            if expectations_form.is_valid():
                expectations = expectations_form.save(commit=False)
                expectations.user_profile = user_profile
                expectations.save()
                return redirect('extra')  # Redirect after saving expectations
    else:
        profile_form = UserProfileForm(instance=user_profile)
        expectations_form = PartnerExpectationsForm(instance=partner_expectations)

    return render(request, 'extra.html', {
        'profile_form': profile_form,
        'expectations_form': expectations_form,
    })

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

