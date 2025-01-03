
from django import forms
from .models import UserRegistration

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Подтвердите пароль")

    class Meta:
        model = UserRegistration
        fields = ["username", "email", "password"]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Пароли не совпадают!")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = self.cleaned_data["password"]
        if commit:
            user.save()
        return user
