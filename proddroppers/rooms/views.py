from django.contrib.auth.models import User
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
            music = request.data["music"]
        except KeyError:
            Response(error_response)

        room = Rooms.objects.create(name=name, current=music)
        return Response(
            {
                "success": True,
                "id": room.id,
                "description": ["Комната создана"],
            }
        )
