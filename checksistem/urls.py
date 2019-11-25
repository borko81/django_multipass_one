from django.urls import path
from checksistem import views

urlpatterns = [
    path('', views.index, name="all_include"),
]
