from django.shortcuts import render, get_object_or_404
from .models import Product

def product_details(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'loja/product_details.html', {'product':product})

