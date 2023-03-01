"""
    To make sure that our models are working properly.
    Let's write some tests.
"""

from django.test import TestCase
from django.urls import reverse
from . models import Book

# Create your tests here.
class BookTestCase(TestCase):
    """ Tests Cases for Book models. """
    @classmethod
    def setUpTestData(cls) -> None:
        cls.book = Book.objects.create(
            title = 'Book1 Test',
            author = 'Book 1 Author',
            price = '99.12',
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
        self.assertContains(response, "Book1 Test")
        self.assertTemplateUsed(response, "books/book_detail.html")
         
         