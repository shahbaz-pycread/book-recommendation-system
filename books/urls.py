from django.urls import path
from . import views  # Import your views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('books/', views.books_list, name='all_books'),
    # Define the URL for book detail view
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('add-book/', views.add_book, name='add-book'),
    path('signup/', views.signup_view, name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name='books/registration/login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout')
]
