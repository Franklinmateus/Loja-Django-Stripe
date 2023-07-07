from django.shortcuts import render
from loja.models import Product

def frontpage(request):
    products = Product.objects.all()[0:]
    return render(request, 'core/frontpage.html', {'products':products})

def sobre(request):
    return render(request, 'core/sobre.html')

