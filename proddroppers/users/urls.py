from django.urls import path

from users.views import DetailAPI


urlpatterns = [
    path(
        "profile/<int:pk>/",
        DetailAPI.as_view(),
    ),
]
