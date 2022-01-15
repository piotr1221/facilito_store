from django.urls import path

from . import views

urlpatterns = [
    # indica el criterio para la busqueda de productos
    path('<slug:slug>', views.ProductDetailView.as_view(), name='product')
]