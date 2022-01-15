from django.contrib import admin

# Register your models here.

from .models import Product

class ProductAdmin(admin.ModelAdmin):
    # se sobreescriben los campos disponibles 
    # para registrar en el modulo de admin
    fields = ('title', 'description', 'price', 'image')
    # se sobreescribe la info que se mostrara
    # en el listado de admin
    list_display = ('__str__', 'slug', 'created_at')


admin.site.register(Product, ProductAdmin)