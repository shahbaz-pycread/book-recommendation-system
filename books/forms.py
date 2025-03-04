from django import forms
from .models import UserRating
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