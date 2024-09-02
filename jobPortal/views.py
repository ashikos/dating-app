from django.shortcuts import render
from django.views.generic import View, TemplateView


# Create your views here.



class LayoutView(TemplateView):
    template_name = 'JobPortal/layout/layout.html'


class DashboardView(TemplateView):
    template_name = 'JobPortal/Candidate/dashboard.html'


class ProfileView(TemplateView):
    template_name = 'JobPortal/Candidate/candidate_profile.html'


class AppliedJobsView(TemplateView):
    template_name = 'JobPortal/Candidate/applied_jobs.html'


class ChangePasswordView(TemplateView):
    template_name = 'JobPortal/Candidate/change_password.html'


class ShortListedJobsView(TemplateView):
    template_name = 'JobPortal/Candidate/short_listed_jobs.html'
