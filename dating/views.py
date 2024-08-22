from django.shortcuts import render
from django.views.generic import TemplateView


class SelectgenderView(TemplateView):
    template_name='Dating/selectgender.html'


class Error403View(TemplateView):
    template_name='error_page/error403.html'
    

class Error404View(TemplateView):
    template_name='error_page/error404.html'
