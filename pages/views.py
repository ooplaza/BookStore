from django.views.generic import TemplateView
from django.shortcuts import render

# Create your views here.
class HomePageView(TemplateView):
    """ Renders the home.html using TemplateView. """
    template_name = "home.html"

class AboutPageView(TemplateView):
    """ Renders the about.html using TemplateView. """
    template_name = "about.html"