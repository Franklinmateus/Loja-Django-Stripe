from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core.views import frontpage, sobre

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('loja.urls')),
    path('', frontpage, name='frontpage'),
    path('sobre', sobre, name='sobre'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
