from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('discover/', DiscoverView.as_view(), name='discover'),   
    path('qualification/', QualificationView.as_view(), name='qualification'),    
    path('location/', LocationView.as_view(), name='location'),   
    path('designation/', DesignationView.as_view(), name='designation'),  
    path('match/', MatchView.as_view(), name='match'),  
    path('profile_view/', ProfileviewView.as_view(), name='profile_view'),  
    path('upgrade/', UpgradeView.as_view(), name='upgrade'),   
    path('spin/', SpinView.as_view(), name='spin'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)