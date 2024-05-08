from django.contrib import admin
from .models import books, book_category, book_author, author, reviews

# Register your models here.
admin.site.register(books)
admin.site.register(book_author)
admin.site.register(book_category)
admin.site.register(author)
admin.site.register(reviews)

