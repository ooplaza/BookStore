"""
    This models uses a one to many relationship.
    ONE BOOK MANY CAN REVIEWS.
"""

import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.
class Book(models.Model):
    """ This model is using uuid for url generation."""
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to="covers/", blank=True)
    
    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        """ Using this method for cannonical urls, much cleaner.

            Instead of using this : <a href="{% url "book_detail" book.id %}">
            Used this for cannonical urls : <a href="{{  book.get_absolute_url }}"> since the pk has aalready been set.
        """
        return reverse("book_detail", args=[str(self.id)])


class Review(models.Model):
    """
        The book field is the one-to-many foreign key
        that links Book to Review and we’re following the standard practice of naming it the same as the
        linked model.
        
        This model Review is associated with Book model above
        
        If you do not specify the related_name argument for the OneToOneField, Django will use the lowercase
        name of the current model as default value.
    """
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="reviews",
        )
    review = models.CharField(max_length=255)
    author = models.ForeignKey(get_user_model(), 
        on_delete=models.CASCADE,
    )
    
    def __str__(self):
        return self.review