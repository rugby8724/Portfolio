from django.shortcuts import render
from django.views import generic
from . models import Job

# Create your views here
class HomePage(generic.TemplateView):
    template_name = 'index.html'
