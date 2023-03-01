import uuid
from django.db import models
from django.urls import reverse

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
    
    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        """ Using this method for cannonical urls, much cleaner.

            Instead of using this : <a href="{% url "book_detail" book.id %}">
            Used this for cannonical urls : <a href="{{  book.get_absolute_url }}"> since the pk has aalready been set.
        """
        return reverse("book_detail", args=[str(self.id)])
    