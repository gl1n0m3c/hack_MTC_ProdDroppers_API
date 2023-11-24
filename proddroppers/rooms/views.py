from django.http import Http404
from django.shortcuts import render
from rooms.models import Rooms


def chatPage(request, room_name):
    try:
        Rooms.objects.get(id=room_name)
    except:
        raise Http404
    context = {"room_name": room_name}
    return render(request, "chatPage.html", context)
