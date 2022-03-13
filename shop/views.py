from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from . import models



def index(request):
    return render(request , 'index.html')


def book(request, slug):
    book_detail = get_object_or_404(models.Book, slug=slug)
    return render(request, 'book.html', {'book_detail': book_detail})
                                            


def author(request, pk):
    author_detail = get_object_or_404(models.Aut, slug=pk)
    return render(request, 'author.html', {'author_detail': author_detail})


def translator(request, pk):
    tr_detail = get_object_or_404(models.Tr, id=pk)
    return render(request, 'translator.html', {'tr_detail': tr_detail})    



