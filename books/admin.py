from django.contrib import admin
from .models import Book

# Customize the admin panel for the Book model
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Define the fields to display in the admin book list
    list_display = ('title', 'author', 'price', 'category', 'published_date')
    
    # Add filters to the admin book list
    list_filter = ('category', 'published_date')
    
    # Enable search functionality in the admin book list
    search_fields = ('title', 'author')
