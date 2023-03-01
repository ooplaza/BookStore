""" 
    class PublisherDetailView(DetailView):

    model = Publisher

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['book_list'] = Book.objects.all()
        return context
    Note

    Generally, get_context_data will merge the context data of all parent classes with those 
    of the current class. To preserve this behavior in your own classes where you want to alter 
    the context, you should be sure to call get_context_data on the super class. When no two classes
    try to define the same key, this will give the expected results. However if any class attempts to override 
    a key after parent classes have set it (after the call to super), any children of that class will also need to 
    explicitly set it after super if they want to be sure to override all parents. If you’re having trouble, review 
    the method resolution order of your view.

    Another consideration is that the context data from class-based generic views will override data provided by context 
    processors; see get_context_data() for an example.
"""


from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . import models

# Create your views here.
class BookListView(ListView):
    """ Returns a rendered list of Book. """
    model = models.Book
    context_object_name = "books"
    template_name = "books/book_list.html"

class BookDetailView(DetailView):
    """ Returns a rendered book detail. """
    model = models.Book
    context_object_name = "book"
    template_name = "books/book_detail.html"