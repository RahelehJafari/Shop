from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.decorators.http import require_POST
from .cart import Cart
from shop import models


@require_POST
def cart_add(requset, book_id):
    cart = Cart(requset)
    book = get_object_or_404(models.Book, id=book_id)
    #form = forms.CartAddBookForm(request.POST)
   # if form.is_valid():
    cart.add(book=book)
    return redirect(reverse('cart:cart_detail'))


def cart_remove(request, book_id):
    cart = Cart(request)
    book = get_object_or_404(models.Book, id=book_id)
    cart.remove(book)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    cart_items = cart.show_cart()
    return render(request, 'cart/detail.html', {'cart': cart_items})

    
