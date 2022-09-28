from django.urls import path

from . import views
app_name = 'Yatube'

urlpatterns = [
    # Главная страница
    path('', views.index),
    path('index.html', views.index, name='index'),
    # Страница с отфильтрофанными группами
    path('group<slug:slug>.<slug:slug>', views.group_posts, name='group'),
]