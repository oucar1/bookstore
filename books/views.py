from django.shortcuts import render, get_object_or_404
from .models import Book
from django.db.models import Q  # For advanced search queries

def book_list(request):
    # Fetch all books
    books = Book.objects.all()
    
    # Filter books by selected category
    selected_category = request.GET.get('category', '')
    if selected_category:
        books = books.filter(category=selected_category)
    
    # Search books by title or author
    query = request.GET.get('q', '')
    if query:
        books = books.filter(title__icontains=query) | books.filter(author__icontains=query)
    
    # Render the book list page with filtered or searched books
    return render(request, 'books/book_list.html', {
        'books': books,
        'categories': Book.CATEGORY_CHOICES
    })

def book_detail(request, pk):
    # Fetch the specific book by primary key (pk)
    book = get_object_or_404(Book, pk=pk)
    
    # Render the book detail page with the selected book
    return render(request, 'books/book_detail.html', {'book': book})

def book_list(request):
    # Fetch books
    books = Book.objects.all()

    # Apply filters
    query = request.GET.get('q', '')
    if query:
        books = books.filter(Q(title__icontains=query) | Q(author__icontains=query))

    category = request.GET.get('category', '')
    if category:
        books = books.filter(category=category)

    sort_order = request.GET.get('sort', '')
    if sort_order == 'asc':
        books = books.order_by('price')
    elif sort_order == 'desc':
        books = books.order_by('-price')

    # Render template
    return render(request, 'books/book_list.html', {
        'books': books,
        'categories': Book.CATEGORY_CHOICES,
        'selected_category': category,
        'sort_order': sort_order,
        'query': query,
    })
