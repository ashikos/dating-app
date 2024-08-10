from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    accept_view,
    contacted_view,
    extra_view,
    messages_view,
    received_view,
    reject_view,
    sent_view,
    shortlist_view,
    shortlisted_view,
    shortlistedby_view,
    viewedmyprofile_view
)
urlpatterns = [
                  path('', views.TestView, name='test'),
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

              ]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)