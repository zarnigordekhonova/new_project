from django.urls import path
from .views import get_info, get_books, detail, add_books, get_reviews, update_books, delete_books, add_review, review_detail


app_name = 'Books'
urlpatterns = [
    path('', get_info, name='get_info'),
    path('books/<int:pk>', get_books, name='get_books'),
    path('books/detail/<int:pk>', detail, name='detail'),
    path('review/<int:pk>', get_reviews, name='get_reviews'),
    path('review/detail/<int:pk>', review_detail, name='review_detail'),
    path('add_books', add_books, name='add_books'),
    path('update/<int:pk>', update_books, name='update_books'),
    path('delete/<int:pk>', delete_books, name='delete_books'),
    path('add/<int:pk>', add_review, name='add_review')
]