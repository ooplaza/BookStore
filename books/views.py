""" 
    USER PERMISSION NEED A DETAILS

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

from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView
from . import models

# Create your views here.
class BookListView(LoginRequiredMixin, ListView):
    """ Returns a rendered list of Book. """
    model = models.Book
    context_object_name = "books"
    # login_url = 'account_login' had already in the settings.py LOGIN_URL
    template_name = "books/book_list.html"

class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    """ Returns a rendered book detail. """
    model = models.Book
    context_object_name = "book"
    # login_url = 'account_login' had already in the settings.py LOGIN_URL
    template_name = "books/book_detail.html"
    permission_required = 'books.special_status'
    

class SearchResultListView(ListView):
    """ This views will render a filtered query data using search. """
    model = models.Book
    context_object_name = "book_search_list"
    template_name = "books/search_results.html"
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        return self.model.objects.filter(
            Q (title__icontains=query) | Q (author__icontains=query) | Q (price__icontains=query)
        )