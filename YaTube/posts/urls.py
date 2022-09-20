from django.urls import path

from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    # Страница с отфильтрофанными группами
    path('groups/', views.group_posts),
    # Страница с постами
    path('posts/', views.posts),
]