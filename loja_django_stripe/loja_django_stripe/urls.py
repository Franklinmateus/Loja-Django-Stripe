from django.contrib import admin
from django.urls import path, include
from core.views import frontpage, sobre

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('loja.urls')),
    path('', frontpage, name='frontpage'),
    path('sobre', sobre, name='sobre'),
]
