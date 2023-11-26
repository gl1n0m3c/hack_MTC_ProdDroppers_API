from django.urls import path
from rooms.views import RoomsAPI


urlpatterns = [
    path("", RoomsAPI.as_view(), name="rooms"),
]
