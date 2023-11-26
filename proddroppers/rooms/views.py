from rest_framework.response import Response
from rest_framework.views import APIView

from rooms.models import Rooms
from rooms.serializers import RoomsSerializer


class RoomsAPI(APIView):
    def get(self, request, *args, **kwargs):
        rooms = Rooms.objects.get_rooms()
        return Response(RoomsSerializer(rooms, many=True).data)
