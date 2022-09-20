from django.urls import path

from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    # Страница с отфильтрофанными группами
    path('group/<slug:slug>/', views.group_posts),
]