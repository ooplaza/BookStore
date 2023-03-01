from django.contrib import admin
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    """ Specifying which fields we want to display on the admin panel.
        In other words we are modifying the admin panel for Books.
    """
    list_display = ("title", "author", "price") 

admin.site.register(Book, BookAdmin)