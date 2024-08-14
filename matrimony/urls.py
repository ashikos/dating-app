from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [

    path('home/', HomeView.as_view(), name='home'),
    path('profileslocation/', ProfilesLocationView.as_view(), name='profiles_location'),
    path('profilesdesignation/', ProfilesDesignationView.as_view(), name='profiles_designation'),
    path('profilesqualification/', ProfilesQualificationView.as_view(), name='profiles_qualification'),
    path('subscriptionplan/', SubscriptionPlanView.as_view(), name='subscription_plan'),
    path('paymentmethods/', PaymentMethodsView.as_view(), name='payment_methods'),
    path('addpaymentmethods/', AddPaymentMethodsView.as_view(), name='add_payment_methods'),
  
  
    path('', TestView, name='test'),
    path('accept/', accept_view, name='accept'),
    path('contacted/', contacted_view, name='contacted'),
    path('extra/', extra_view, name='extra'),
    path('messages/', messages_view, name='messages'),
    path('received/', received_view, name='received'),
    path('reject/', reject_view, name='reject'),
    path('sent/', sent_view, name='sent'),
    path('shortlist/', shortlist_view, name='shortlist'),
    path('shortlisted/', shortlisted_view, name='shortlisted'),
    path('shortlistedby/', shortlistedby_view, name='shortlistedby'),
    path('viewedmyprofile/', viewedmyprofile_view, name='viewedmyprofile'),
    
    
    path('profiledescription/', ProfileDescription.as_view(), name='profiledescription'),
    path('edit_profile/', EditProfile.as_view(), name='edit_profile'),
    path('change_password/',ChangePasswordView.as_view(),name='change_password'),
    path('settings/',SettingsView.as_view(),name='settings'),
    path('privacy/',PrivacySettingsView.as_view(),name='privacy'),
    path('partner_preferences/',PartnerView.as_view(),name='partner_preferences'),

]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)