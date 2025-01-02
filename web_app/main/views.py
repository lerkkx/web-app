from django.shortcuts import render
from .models import Registration



def index(request):
    reg_inf = Registration.objects.all() # отсюда можно их и записать в бд кстати а бля это ж из бд
    return render(request, "main/index.html")


def about(request):
    return render(request, "main/about.html")