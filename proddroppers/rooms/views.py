from django.shortcuts import render


def chatPage(request, room_name):
    context = {"room_name": room_name}
    return render(request, "chatPage.html", context)
