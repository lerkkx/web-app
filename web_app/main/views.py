from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm, LoginForm
from .models import UserRegistration

def index(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')
        else:
            return render(request, 'main/index.html', {'form': form, 'errors': form.errors})
    else:
        form = RegistrationForm()
    return render(request, 'main/index.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('about')  # ПОМЕНЯТЬ НА ОСНОВНУЮ СТРАНИЦУ
            else:
                return render(request, 'main/login.html', {'form': form, 'error': "Неверное имя пользователя или пароль."})
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})

def about(request):
    return render(request, 'main/about.html')
