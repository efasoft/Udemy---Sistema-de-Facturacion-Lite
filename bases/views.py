from django.shortcuts import render
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Create your views here.
class Home(LoginRequiredMixin,TemplateView):
    template_name = 'bases/home.html'
    login_url = 'config:login'
