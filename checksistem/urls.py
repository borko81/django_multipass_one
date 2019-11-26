from django.urls import path
from checksistem import views

urlpatterns = [
	# URL's
	# Начална страница
    path('', views.index, name="begin"),
    # Конфигурация на карти
    path('cards/', views.cards, name="cards"),
    # Конфигурация на групи
    path('groups/', views.groups, name="groups"),
    # Конфигурация на служители
    path('employe/', views.groups, name="groups"),
]
