from django.urls import path

from users_auth.views import RegisterUserAPIView, UserDetailAPI

urlpatterns = [
    path("get-details", UserDetailAPI.as_view()),
    path("register", RegisterUserAPIView.as_view()),
]
