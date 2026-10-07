from django.http import HttpResponse


def index(request):
    return HttpResponse("Привет, Django! Приложение работает.")