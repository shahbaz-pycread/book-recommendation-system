from django.urls import path
from . import views  # Import your views

urlpatterns = [
    path('books/', views.books_list, name='all_books'),
    # Define the URL for book detail view
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
]
