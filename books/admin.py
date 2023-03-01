from django.contrib import admin
from .models import Book, Review

# Register your models here.
class ReviewInline(admin.TabularInline):
    """ The TabularInline displays data in table. """
    model = Review

class BookAdmin(admin.ModelAdmin):
    """ Specifying which fields we want to display on the admin panel.
        In other words we are modifying the admin panel for Books.
    """
    inlines = [
        ReviewInline,
    ]
    list_display = ("title", "author", "price") 

admin.site.register(Book, BookAdmin)