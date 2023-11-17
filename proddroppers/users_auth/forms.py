from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm,
    UserChangeForm, UserCreationForm)
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Логин"}),
    )
    email = forms.CharField(
        label="",
        widget=forms.EmailInput(attrs={"placeholder": "E-mail"}),
    )
    password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={"placeholder": "Пароль"}),
    )
    password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={"placeholder": "Повторите пароль"}),
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Логин"}),
    )
    password = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={"placeholder": "Пароль", "class": "form-control"}),
    )


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={"placeholder": "Старый пароль"}),
    )
    new_password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={"placeholder": "Новый пароль"}),
    )
    new_password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={"placeholder": "Повторите новый пароль"}),
    )

    class Meta:
        model = User
        fields = ("old_password", "new_password1", "new_password2")


class ChangeUserDataForm(UserChangeForm):
    username = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Логин"}),
    )
    email = forms.EmailField(
        label="",
        required=False,
        widget=forms.EmailInput(attrs={"placeholder": "E-mail"}),
    )
    password = None

    class Meta:
        model = User
        fields = ("username", "email")
