from django.contrib import admin
from .models import Book, UserRating
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ['title','author','genre','rating']
    list_filter = ['author','genre']
    search_fields = ['author','genre']
    
admin.site.register(Book,BookAdmin)

class UserRatingAdmin(admin.ModelAdmin):
    list_display = ['user','book','rating']
    
admin.site.register(UserRating,UserRatingAdmin)
