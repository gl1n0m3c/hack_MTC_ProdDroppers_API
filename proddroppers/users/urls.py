from django.urls import path
from users.views import UserDetailAPI


urlpatterns = [
    path("get_details/<int:pk>/", UserDetailAPI.as_view()),
]
