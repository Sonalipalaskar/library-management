from django.shortcuts import render
from .models import Book, Borrower

def book_list(request):
    books = Book.objects.all()
    return render(request, 'library_app/templates/book_list.html', {'books': books})

def borrower_list(request):
    borrowers = Borrower.objects.all()
    return render(request, 'library_app/templates/borrower_list.html', {'borrowers': borrowers})
