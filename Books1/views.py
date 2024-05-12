from django.shortcuts import render, redirect, get_object_or_404
from .models import books, book_category, reviews
from .forms import booksForm, reviewsForm


# Create your views here.

def get_info(request):
    categories = book_category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'index.html', context=context)

def get_books(request, pk):
    products = books.objects.filter(genre=pk)
    context = {
        'products': products
    }
    return render(request, 'books.html', context=context)


def get_reviews(request, pk):
    items = reviews.objects.filter(book_title=pk)
    context = {
        'items': items
    }
    return render(request, 'reviews.html', context)

def review_detail(request, pk):
    item = reviews.objects.get(pk=pk)
    context = {
        'item' : item
    }
    return render(request, 'review_detail.html', context=context)



def detail(request, pk):
    product = books.objects.get(pk=pk)
    context = {
        'product': product
    }
    return render(request, 'detail.html', context=context)

def add_books(request):
    form = booksForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('Books:get_info')
    context = {
        'form': form
    }
    return render(request, 'create.html', context=context)

def update_books(request, pk):
    data = books.objects.get(pk=pk)
    form = booksForm(request.POST, request.FILES, instance=data)
    if form.is_valid():
        print(1)
        form.save()
        return redirect('Books:get_info')
    context = {
        'form': form
    }
    return render(request, 'update.html', context=context)

def delete_books(request, pk):
    product = get_object_or_404(books, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('Books:get_info')

    return render(request, 'delete.html', {'product': product})


def add_review(request, pk):
    # data = reviews.objects.get(book_title=pk)
    form = reviewsForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('Books:get_info')
    context = {
        'form': form
    }
    return render(request, 'add_review.html', context=context)



