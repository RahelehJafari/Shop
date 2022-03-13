from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Book(models.Model):
    type_Coiches = {('V', 'voice'), ('T', 'text')}
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    author = models.ManyToManyField('Aut', blank = False)
    translator = models.ManyToManyField('Tr', blank = True)
    publisher = models.CharField(max_length=100)
    description = models.TextField(null=True)
    published_year = models.IntegerField(null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('cat', blank=True)
    ISBN = models.IntegerField(null=True)
    type = models.CharField(choices=type_Coiches, max_length=1, blank=True)
    pages = models.IntegerField(null=True)
    image = models.ImageField(upload_to='images/product/%Y/%m/%d', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)

    

    class Meta:
        ordering = ('create_time',)

    

    def get_absolute_url(self):
        return reverse('shop:book', args=[self.id])


class Aut(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True)

     
    def __str__(self):
      return self.name

class Tr(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True)
     
    def __str__(self):
      return self.name

class Cat(models.Model):
    name = models.CharField(max_length=50)
     
    def __str__(self):
      return self.name


class Pub(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='images/publogo', blank=True)
    description = models.TextField(null=True)
     
    def __str__(self):
      return self.name

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, null=True, on_delete=models.SET_NULL)
    book_price = models.DecimalField(max_digits=10, decimal_places=0)
    
    def __str__(self):
        return str(self.id)


class Invoice(models.Model):
    order = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)
    invoice_date = models.DateTimeField(auto_now_add=True)
    authority = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.id)


class Transaction(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('failed', 'Failed'),
        ('completed', 'Completed')
    )
    invoice = models.ForeignKey(Invoice, null=True, on_delete=models.SET_NULL)
    transaction_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return str(self.id)

