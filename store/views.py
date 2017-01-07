from django.shortcuts import render
from .models import Book
# Create your views here.


def books_list(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})

