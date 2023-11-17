from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import redirect
from django.urls.base import reverse_lazy
from django.views.generic import CreateView, UpdateView

from users_auth.forms import (
    ChangePasswordForm, ChangeUserDataForm,
    LoginForm, SignUpForm)


class SignUpPage(CreateView):
    form_class = SignUpForm
    template_name = "users/form.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Регистрация"
        context["button_text"] = "Зарегистрироваться"
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("login")


class LoginPage(LoginView):
    form_class = LoginForm
    template_name = "users/form.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Вход"
        context["button_text"] = "Войти"
        context["noaccount_text"] = "Нет аккаунта? "
        context["signupurl"] = "Создайте!"
        return context

    def get_success_url(self):
        return reverse_lazy("login")


class ChangeUserDataPage(LoginRequiredMixin, UpdateView):
    form_class = ChangeUserDataForm
    template_name = "users/form.html"
    success_url = reverse_lazy("login")
    login_url = reverse_lazy("login")

    def get_object(self):
        return self.request.user

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Редактировать данные"
        context["button_text"] = "Сохранить"
        return context


class ChangePasswordPage(LoginRequiredMixin, PasswordChangeView):
    form_class = ChangePasswordForm
    template_name = "users/form.html"
    login_url = reverse_lazy("login")
    success_url = reverse_lazy("login")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Изменить пароль"
        context["button_text"] = "Изменить"
        return context

    def form_valid(self, form):
        return super().form_valid(form)


def logout_user(request):
    logout(request)
    return redirect("login")
