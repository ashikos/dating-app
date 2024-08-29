from django.urls import path
from jobPortal import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'jobportal'

urlpatterns = [
                  path('',views.home),
                  path('about/',views.about),
                  path('contact/',views.contact),
                  path('register/',views.user_register,name='register'),
                  path('login/',views.login,name='login'),
                  path('job-details/',views.job_details,name='job_details'),
                  
              ]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)