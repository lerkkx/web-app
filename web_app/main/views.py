from django.shortcuts import render
from .models import Registration



def index(request):
    return render(request, "main/index.html")


def about(request):
    return render(request, "main/about.html")