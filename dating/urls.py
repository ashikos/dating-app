from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'Dating'
urlpatterns = [
                path("", views.SelectgenderView.as_view(), name="selectgender"),
                path("error403", views.Error403View.as_view(), name="error403"),
                path("error404", views.Error404View.as_view(), name="error404"),
              ]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)