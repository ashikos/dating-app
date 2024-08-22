from django.shortcuts import render
from django.views.generic import View, TemplateView


# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

class DiscoverView(TemplateView):
    template_name = 'discover.html'

class QualificationView(TemplateView):
    template_name = 'qualification.html'

class LocationView(TemplateView):
    template_name = 'location.html'

class DesignationView(TemplateView):
    template_name = 'designation.html'

class MatchView(TemplateView):
    template_name = 'matches.html'

class ProfileviewView(TemplateView):
    template_name = 'profileviews.html'

class UpgradeView(TemplateView):
    template_name = 'upgradepage.html'

class SpinView(TemplateView):
    template_name = 'spin.html'