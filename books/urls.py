from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),  # Route for the book list view
    path('book/<int:pk>/', views.book_detail, name='book_detail'),  # Route for the book detail view
]
