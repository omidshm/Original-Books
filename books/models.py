from django.db import models

# Create your models here.

class Book(models.Model):
    """
        Book representing a book.
    """
    isbn = models.CharField(max_length=13, unique=True, primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_date = models.DateField()
    # Add more book-related fields as needed
