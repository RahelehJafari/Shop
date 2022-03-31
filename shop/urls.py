from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='home'),
    path('book/<slug>/', views.book, name='book'),
    path('author/<int:pk>/', views.author, name='author'),
    path('translator/<int:pk>/', views.translator, name='translator'),
    path('categories/', views.categories , name='categories'),  
    path('categories/<slug>/', views.cat , name='cat'),
 
]
