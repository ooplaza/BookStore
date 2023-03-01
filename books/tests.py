"""
    To make sure that our models are working properly.
    Let's write some tests.
"""

from django.test import TestCase
from django.urls import reverse
from . models import Book, Review
from django.contrib.auth import get_user_model

# Create your tests here.
class BookTestCase(TestCase):
    """ Tests Cases for Book models. """
    @classmethod
    def setUpTestData(cls) -> None:
        # Create a user that will be used for reviews
        """
            objects.create_user() is a method of the user model that
            creates and saves a new user with the specified email and password.
        """
        cls.user = get_user_model().objects.create_user(
            username = 'reviewuser',
            email = 'reviewuserv@email.com',
            password = 'reviewuser321',
        )
        
        # Create a Book model
        cls.book = Book.objects.create(
            title = 'Book1 Test',
            author = 'Book 1 Author',
            price = '99.12',
        )
        
        # Creating a test reviews for the created book and user.
        cls.review = Review.objects.create(
            book = cls.book,
            author = cls.user,
            review = "An exelent test review."
        )
    
    def test_book_listing(self):
        """ This methods is responsible for testing the book creation. """
        self.assertEqual(f"{self.book.title}", "Book1 Test")
        self.assertEqual(f"{self.book.author}", "Book 1 Author")
        self.assertEqual(f"{self.book.price}", "99.12")
    
    def test_book_list_view(self):
        """ This method is responsible for testing the book list view. """
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Book1 Test")
        self.assertTemplateUsed(response, "books/book_list.html")
    
    def test_book_detail_view(self):
        """ This method is responsible for testing the book detail view. """
        response = self.client.get(self.book.get_absolute_url())
        no_respose = self.client.get("/books/121212/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_respose.status_code, 404)
        self.assertContains(response, "An exelent test review.")
        self.assertContains(response, "Book1 Test")
        self.assertTemplateUsed(response, "books/book_detail.html")
         
         