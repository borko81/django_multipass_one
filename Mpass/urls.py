from django.contrib import admin
# Добавени са url-ите от проект checksistem
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('checksistem.urls')),
]
