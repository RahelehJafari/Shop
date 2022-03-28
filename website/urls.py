from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('shop.urls')),
    path('admin/', admin.site.urls),
    path('book/<int:pk>/', include('shop.urls')),
    path('author/', include('shop.urls')),
    path('translator/', include('shop.urls')),
    path('accounts/', include('accounts.urls')),
    path('cart/', include('cart.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



#urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('', views.index , name="home"),
    

#]
