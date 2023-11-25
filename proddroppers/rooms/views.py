from django.http import Http404
from django.shortcuts import render
from rooms.models import Rooms
from users_music.models import Music


def chat_page(request, room_id):
    try:
        Rooms.objects.get(id=room_id)
    except:
        raise Http404
    context = {"room_id": room_id, "music": Music.objects.get(id=2)}
    return render(request, "chatPage.html", context)
