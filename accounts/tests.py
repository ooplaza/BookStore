"""
    Two Main Types of Test:
        Unit Test : small, fast and isolated to a specific piece of functionality
        Integration Test : Large, slow and used for testing an entire application or a user flow
                           Like payment that covers multiple screens
"""

from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
from .views import SignupPageView
from .forms import CustomUserCreationForm
from django.test import TestCase

# Create your tests here.
class CustomUserTests(TestCase):
    """ This class will resposible for testing in creating normal user and a superuser. """
    def test_create_user(self):
        """ A Custom Test for creating a normal user. """
        User = get_user_model()
        user = User.objects.create_user(
            username="test1", email="test1@gmail.com", password="test1"
        )
        
        self.assertEqual(user.username, 'test1')
        self.assertEqual(user.email, 'test1@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
    
    def test_create_superuser(self):
        """ A Custom Test for creating a superuser. """
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='admin', email='admin@gmail.com', password="admin321"
        )
         
        self.assertEqual(admin_user.username, 'admin')
        self.assertEqual(admin_user.email, 'admin@gmail.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class SignupPageTest(TestCase):   
    """ Testing for signing up. """ 
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)
    
    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "registration/signup.html")
        self.assertContains(self.response, "Sign Up")
        self.assertNotContains(self.response, 'Hi there! I should not be on the page')
    
    def test_signup_form(self):
        """ Test if the CustomUserCreationForm is being utilized || used. """
        form = self.response.context.get("form")
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, "csrfmiddlewaretoken")

    def test_signup_view(self): # new
        view = resolve("/accounts/signup/")
        self.assertEqual(view.func.__name__, SignupPageView.as_view().__name__)