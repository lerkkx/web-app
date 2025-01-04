from django.shortcuts import render, redirect
from .forms import RegistrationForm

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
    return render(request, 'main/login.html')

def about(request):
    return render(request, 'main/about.html')
