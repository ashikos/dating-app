from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import *

urlpatterns = [
    path('', views.TestView, name='test'),

    path('home/', HomeView.as_view(), name='home'),
    path('profileslocation/', ProfilesLocationView.as_view(), name='profiles_location'),
    path('profilesdesignation/', ProfilesDesignationView.as_view(), name='profiles_designation'),
    path('profilesqualification/', ProfilesQualificationView.as_view(), name='profiles_qualification'),
    path('subscriptionplan/', SubscriptionPlanView.as_view(), name='subscription_plan'),
    path('paymentmethods/', PaymentMethodsView.as_view(), name='payment_methods'),
    path('addpaymentmethods/', AddPaymentMethodsView.as_view(), name='add_payment_methods'),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)