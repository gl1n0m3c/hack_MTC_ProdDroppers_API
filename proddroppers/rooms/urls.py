from django.urls import path
from rooms.views import RoomsAPI


urlpatterns = [
    path("", RoomsAPI.as_view(), name="rooms"),
    path("create/", RoomsAPI.as_view(), name="rooms_create"),
]
