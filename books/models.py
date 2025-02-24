from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=155)
    description = models.TextField()
    genre = models.CharField(max_length=100)
    rating = models.FloatField()
    
    def __str__(self):
        return self.title
    
class UserRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i,i) for i in range(1,6)])
    
    def __str__(self):
        return f"{self.user.username} rated {self.book.title} - {self.rating}"
