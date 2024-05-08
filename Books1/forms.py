from django.forms import ModelForm
from .models import books, reviews, author

class booksForm(ModelForm):
    class Meta:
        model = books
        fields = '__all__'

class reviewsForm(ModelForm):
    class Meta:
        model = reviews
        fields = '__all__'

class authorForm(ModelForm):
    class Meta:
        model = author
        fields = '__all__'