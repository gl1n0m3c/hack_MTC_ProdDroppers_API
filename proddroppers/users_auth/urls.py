from django.urls import path

from users_auth.views import RegisterUserAPIView

urlpatterns = [
    path("register", RegisterUserAPIView.as_view()),
]
