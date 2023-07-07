from django.shortcuts import render
from .models import Product

def product_details(request):
    return render(request, 'loja/product_details.html')
