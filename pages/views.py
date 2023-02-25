from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


# class based function
class HomePage(TemplateView):
    template_name = 'home.html'


# about page
class AboutPage(TemplateView):
    template_name = 'about.html'
