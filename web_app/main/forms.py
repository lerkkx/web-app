from django import forms
from .models import UserRegistration

class RegistrationForm(forms.ModelForm):
    username = forms.CharField(label="Имя пользователя:")
    email = forms.EmailField(label="Электронная почта:")
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Подтвердите пароль")

    class Meta:
        model = UserRegistration
        fields = ["username", "email", "password", "confirm_password"]
        error_messages = {
            'username': {
                'unique': "Пользователь с таким именем уже существует.",
            },
            'email': {
                'unique': "Пользователь с такой электронной почтой уже существует.",
            },
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if UserRegistration.objects.filter(username=username).exists():
            raise forms.ValidationError("Пользователь с таким именем уже существует.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if UserRegistration.objects.filter(email=email).exists():
            raise forms.ValidationError("Пользователь с такой электронной почтой уже существует.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Пароли не совпадают!")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])  # хешируем пароль
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class PasswordResetRequestForm(forms.Form):
    email = forms.EmailField(label="Электронная почта:")

class SetPasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput, label="Новый пароль")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Подтвердите новый пароль")

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Пароли не совпадают!")
        return cleaned_data
