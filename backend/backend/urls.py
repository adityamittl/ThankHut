from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('send', send),
    path('note', note),
    path('', include('auth0login.urls')),
    path('', index, name='index')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
