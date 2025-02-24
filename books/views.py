from django.shortcuts import render, get_object_or_404
from .models import Book
from .recommendations import recommend_books

# Create your views here.

def books_list(request):
    books = Book.objects.all()
    context = {
        'books' : books
    }
    return render(request,'books/book_list.html',context)

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    # Get recommendation for this book
    recommended_books = recommend_books(book.title)
    context = {
        'book' : book,
        'recommended_books' : recommended_books
    }
    return render(request, 'books/book_detail.html', context)
