from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, UserRating
from .recommendations import recommend_books
from .forms import RatingForm
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
    
    # Handling Rating form
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.book = book
            rating.user = request.user # Associate the rating with the current user
            rating.save()
            return redirect('book_detail', book_id = book_id) # Refresh the page after form submission
    else:
        form = RatingForm()
        
    # Get all existing ratings for this book
    ratings = UserRating.objects.filter(book=book)
    context = {
        'book' : book,
        'recommended_books' : recommended_books,
        'form' : form,
        'ratings' : ratings
    }
    return render(request, 'books/book_detail.html', context)

