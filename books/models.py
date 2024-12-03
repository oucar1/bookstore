from django.db import models

class Book(models.Model):
    CATEGORY_CHOICES = [
        ('Fiction', 'Fiction'),
        ('Non-Fiction', 'Non-Fiction'),
        ('Poetry and Literature', 'Poetry and Literature'),
        ('Technical and Professional', 'Technical and Professional'),
        ('Academic and Education', 'Academic and Education'),
    ]  # Predefined categories

    title = models.CharField(max_length=200)  # Book title
    author = models.CharField(max_length=100)  # Author name
    description_short = models.TextField()  # Short description
    description_long = models.TextField()  # Long description
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price
    image = models.ImageField(upload_to='book_images/')  # Book image
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)  # Category dropdown
    published_date = models.CharField(max_length=7, help_text="Format: YYYY-MM")  # Published date (Year-Month)

    def __str__(self):
        return self.title
