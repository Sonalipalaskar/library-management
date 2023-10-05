from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_year = models.PositiveIntegerField()
    isbn = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.title

class Borrower(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    borrowed_books = models.ManyToManyField(Book, blank=True)

    def __str__(self):
        return self.name