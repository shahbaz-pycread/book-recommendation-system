from django import forms
from .models import UserRating, Book
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RatingForm(forms.ModelForm):
    class Meta:
        model = UserRating
        fields = ['rating', 'comment']
        
class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username','email','password1', 'password2']
        
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'genre', 'rating', 'image']
        widgets = {
            'description' : forms.Textarea(attrs={'rows' : 4}),
            'rating' : forms.NumberInput(attrs={'min' : 0, 'max' : 5})
        }