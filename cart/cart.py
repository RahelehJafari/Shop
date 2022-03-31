from django.conf import settings
from decimal import Decimal
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

    def remove(self, book):
        book_id = str(book.id)
        if book_id in self.cart:
            del self.cart[book_id]
            self.save()     
    
    def show_cart(self):
        book_ids = self.cart.keys()
        books = models.Book.objects.filter(id__in=book_ids)

        for book in books:
            self.cart[str(book.id)]['book']= book

        for item in self.cart.values():
            item['price'] =Decimal(item['price'])   
        return self.cart.values()

    def save(self):
        self.session[settings.CART_SESSION_ID]= self.cart
        self.session.modified = True

    def get_total_price(self):
        return sum(Decimal(item['price']) for item in self.cart.values() )    

                