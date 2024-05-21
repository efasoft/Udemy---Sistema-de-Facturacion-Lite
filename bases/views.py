from django.shortcuts import render
from django.views.generic import *

# Create your views here.
class Home(TemplateView):
    template_name = 'bases/home.html'
    login_url = 'config:login'
