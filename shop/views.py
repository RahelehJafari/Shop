from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from . import models
from cart.forms import CartAddBookForm



def index(request):
    return render(request , 'index.html')


def book(request, slug):
    book_detail = get_object_or_404(models.Book, slug=slug)
    cart_add_book_form = CartAddBookForm()
    return render(request, 'book.html', {'book_detail': book_detail, 'cart_add_book_form':cart_add_book_form})
                                            


def author(request, pk):
    author_detail = get_object_or_404(models.Aut, slug=pk)
    return render(request, 'author.html', {'author_detail': author_detail})


def translator(request, pk):
    tr_detail = get_object_or_404(models.Tr, id=pk)
    return render(request, 'translator.html', {'tr_detail': tr_detail})    



