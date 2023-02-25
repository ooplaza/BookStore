# This isn't needed anymore because django-allauth did the job already for the routes

from . forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Create your views here.
class SignupPageView(CreateView):
    """ Inheriting the CustomUserCreationForm. """
    # After creating an account user will be redirected to the login page, via success_url.
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"