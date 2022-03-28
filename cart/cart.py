from django.conf import settings
from shop import models

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('settings.CART_SESSION_ID')
        if not cart:
            cart = self.session['settings.CART_SESSION_ID'] = {}
        self.cart = cart    

    def add(self, book):
        book_id = str(book.id)
        if book_id not in self.cart:
            self.cart[book_id]={'price': str(book.price)}
        self.save()
    
    def show_cart(self):
        book_ids = self.cart.keys()
        books = models.Book.objects.filter(id__in=book_ids)
        return books

    def save(self):
        self.session[settings.CART_SESSION_ID]= self.cart
        self.session.modified = True

                