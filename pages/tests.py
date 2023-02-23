"""
    Django SimpleTestCase54 which is a special subset
    of Django TestCase that is designed for webpages that do not have a model included.    
"""

from .views import HomePageView
from django.urls import reverse, resolve
from django.test import SimpleTestCase

# Create your tests here.
class HomepageTest(SimpleTestCase):
    def setUp(self):
        url = reverse("Home")
        self.response = self.client.get(url)
    
    def test_url_exist_at_correct_location(self):
        """ Test for correct location of the home directory. """
        self.assertEqual(self.response.status_code, 200)

    # def test_homepage_url_name(self):
    #     """ Test for correct name in urls using reverse. """
    #     response = self.client.get(reverse('Home'))
    #     self.assertEqual(response.status_code, 200)
    
    def test_homepage_template(self):
        """ Test if that templates exist. """
        self.assertTemplateUsed(self.response, "home.html")
        
    def test_homepage_does_not_contain_incorrect(self):
        """ Test for incorrect text possibility. """
        self.assertContains(self.response, "home page")
    
    def test_homepage_does_not_contain_incorrect_html(self):
        """ To ensure that second parameter isn't in the homepage."""
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")
    
    def test_homepage_url_resolves_homepageview(self):
        """ Refers to the process of matching a requested URL. """
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)
    
    
    
    
    
    
    
    
    
    
    
    