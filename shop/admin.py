from django.contrib import admin

from . import models

admin.site.register(models.Book)
admin.site.register(models.Order)
admin.site.register(models.OrderItem)
admin.site.register(models.Invoice)
admin.site.register(models.Transaction)
admin.site.register(models.Aut)
admin.site.register(models.Tr)
admin.site.register(models.Cat)
admin.site.register(models.Pub)



