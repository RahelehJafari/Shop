from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from . import models
from cart.forms import CartAddBookForm



def index(request):
    return render(request , 'index.html')

def categories(request):
    cats = models.Cat.objects.all()
    return render(request, 'categories.html', {'cats':cats})    


def book(request, slug):
    book_detail = get_object_or_404(models.Book, slug=slug)
    cart_add_book_form = CartAddBookForm()
    return render(request, 'book.html', {'book_detail': book_detail, 'cart_add_book_form':cart_add_book_form})

def cat(request, slug):
    c=models.Cat.objects.get(slug=slug)
    books=models.Book.objects.filter(categories=c)
    cat_list = get_object_or_404(models.Cat, slug=slug)
    return render(request, 'cat.html', {'cat_list': cat_list, 'books': books})                                  


def author(request, pk):
    author_detail = get_object_or_404(models.Aut, slug=pk)
    return render(request, 'author.html', {'author_detail': author_detail})


def translator(request, pk):
    tr_detail = get_object_or_404(models.Tr, id=pk)
    return render(request, 'translator.html', {'tr_detail': tr_detail})    



