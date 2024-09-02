from django import views
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'jobs'

urlpatterns = [
        # path('', views.TestView, name='test'),
        path('layout/',LayoutView.as_view(), name='layout'),
        path('dash_view/',DashboardView.as_view(), name='dash_view'),
        path('profile_view/',ProfileView.as_view(), name='profileview'),
        path('applied_jobs/',AppliedJobsView.as_view(), name='applied_jobs'),
        path('change_password/',ChangePasswordView.as_view(), name='change_password'),
        path('short_listed_jobs/',ShortListedJobsView.as_view(), name='short_lists'),

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)