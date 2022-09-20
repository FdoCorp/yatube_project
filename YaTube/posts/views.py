from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')


def group_posts(request):
    return HttpResponse('Страница групп')

def posts(request):
    return HttpResponse('Страница с постами')