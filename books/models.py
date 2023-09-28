from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Book(models.Model):
    isbn = models.CharField(primary_key=True, max_length=13)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_date = models.DateField()
    pages_number = models.PositiveIntegerField()
    cover_type = models.CharField(max_length=255)
    paper_type = models.CharField(max_length=255)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    size_type = models.CharField(max_length=255)

class BookItem(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

# The rest of your Books app models can go here if needed.
