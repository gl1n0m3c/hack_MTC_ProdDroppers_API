from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from rooms.models import Rooms, UsersRooms
from rooms.serializers import RoomsSerializer


error_response = {
    "success": False,
    "description": ["Ты отправил мне какую-то дичь"],
}


class RoomsAPI(APIView):
    def get(self, request, *args, **kwargs):
        rooms = Rooms.objects.get_rooms()
        return Response(RoomsSerializer(rooms, many=True).data)

    def post(self, request, *args, **kwargs):
        try:
            name = request.data["name"]
        except KeyError:
            Response(error_response)

        Rooms.objects.create(name=name)
        return Response({"success": True, "description": ["Комната создана"]})


def chat_page(request, room_id):
    try:
        room = Rooms.objects.get(id=room_id)
    except Rooms.DoesNotExist:
        raise Http404
    context = {"room_name": room_id}
    context = {"room_id": room_id, "music": room.current}
    return render(request, "chatPage.html", context)
