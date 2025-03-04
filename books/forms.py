from django import forms
from .models import UserRating

class RatingForm(forms.ModelForm):
    class Meta:
        model = UserRating
        fields = ['rating', 'comment']