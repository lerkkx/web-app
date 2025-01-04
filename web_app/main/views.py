from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponse
from django.utils import timezone
from datetime import timedelta
from .forms import RegistrationForm, LoginForm, PasswordResetRequestForm, SetPasswordForm
from .models import UserRegistration
from django.conf import settings


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
                return redirect('about') #ПОМЕНЯТЬ НА ОСНОВНУЮ СТРАНИЦУ
            else:
                try:
                    user = UserRegistration.objects.get(username=username)
                    return render(request, 'main/login.html', {'form': form, 'error': "Неверный пароль."})
                except UserRegistration.DoesNotExist:
                    return render(request, 'main/login.html', {'form': form, 'error': "Пользователь с таким именем не найден."})
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})


def about(request):
    return render(request, 'main/about.html')


def make_token_with_expiry(user): #фиксируем время отправки письма + генерируем ссылку
    token = default_token_generator.make_token(user)
    user.token_timestamp = timezone.now()
    user.save()
    return token


def is_token_valid(user, token): #проверяем ссылку на истечение времени
    if default_token_generator.check_token(user, token):
        expiry_time = user.token_timestamp + timedelta(minutes=10)
        return timezone.now() <= expiry_time
    return False


def password_reset_request(request): #получение почты пользователя и отправки письма
    if request.method == "POST":
        form = PasswordResetRequestForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            associated_users = UserRegistration.objects.filter(email=email)
            if associated_users.exists():
                for user in associated_users:
                    subject = "Восстановление пароля"
                    email_template_name = "main/password_reset_email.txt"
                    data = {
                        "email": user.email,
                        'domain': request.get_host(),
                        'site_name': 'Ваш сайт',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': make_token_with_expiry(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, data)
                    try:
                        send_mail(subject, email, settings.DEFAULT_FROM_EMAIL, [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("password_reset_done")
    else:
        form = PasswordResetRequestForm()
    return render(request, "main/password_reset.html", {"form": form})

def password_reset_done(request):
    return render(request, 'main/password_reset_done.html')

def password_reset_confirm(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = UserRegistration.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, UserRegistration.DoesNotExist):
        user = None
    if user is not None and is_token_valid(user, token):
        if request.method == 'POST':
            form = SetPasswordForm(request.POST)
            if form.is_valid():
                user.set_password(form.cleaned_data['password'])
                user.save()
                return redirect('password_reset_complete')
        else:
            form = SetPasswordForm()
        return render(request, 'main/password_reset_confirm.html', {'form': form})
    else:
        return render(request, 'main/password_reset_expired.html', {'error_message': "Ссылка для восстановления пароля истекла. Пожалуйста, запросите новую ссылку для восстановления пароля."})
def password_reset_complete(request):
    return render(request, 'main/password_reset_complete.html')