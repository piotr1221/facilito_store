from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Product
# Create your views here.

class ProductListView(ListView):
    # estas dos variables tienen nombres predefinidos
    template_name = 'index.html'
    queryset = Product.objects.all().order_by('-id')

    # se puede modificar el context que pasa al template,
    # sino tendra por defecto unicamente el queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Listado de productos'
        return context

# muestra informacion de un objeto en particular
# por defecto usa el id que viene mediante la ruta
class ProductDetailView(DetailView):
    template_name = 'products/product.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 4 * context['object'].price
        return context