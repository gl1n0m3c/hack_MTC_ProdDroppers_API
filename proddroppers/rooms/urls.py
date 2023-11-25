from django.urls import path, include
from rooms import views as chat_views


urlpatterns = [
    path("<int:room_id>/", chat_views.chat_page, name="chat-page"),
]
