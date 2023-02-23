"""
    Two Main Types of Test:
        Unit Test : small, fast and isolated to a specific piece of functionality
        Integration Test : Large, slow and used for testing an entire application or a user flow
                           Like payment that covers multiple screens
"""

from django.contrib.auth import get_user_model
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