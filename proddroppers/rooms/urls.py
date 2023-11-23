from django.urls import path, include
from rooms import views as chat_views


urlpatterns = [
    path("<int:room_name>/", chat_views.chatPage, name="chat-page"),
]
