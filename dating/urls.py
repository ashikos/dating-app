from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('test', views.TestView, name='test'),
    path('story/', views.StoryPageView.as_view(), name='story'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('change_password/', views.ChangePasswordView.as_view(), name='change_password'),
    path('upgrade/',views.UpgradeStoryView.as_view(),name="upgrade")
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)