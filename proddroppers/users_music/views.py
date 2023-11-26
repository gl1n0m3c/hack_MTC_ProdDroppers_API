from rest_framework.response import Response
from rest_framework.views import APIView

from users_music.models import Music
from users_music.serializer import MusicSerializer


error_response = {
    "success": False,
    "description": ["Ты отправил мне какую-то дичь"],
}


class MusicAPI(APIView):
    def get(self, request, pk, *args, **kwargs):
        try:
            music = Music.objects.get_one_music(pk=pk)
        except Music.DoesNotExist:
            return Response(error_response)

        serializer = MusicSerializer(music[0])

        return Response({"success": True, "data": serializer.data})


class MusicListAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            page = request.GET.get("page")
            if page is None:
                page = 0
            else:
                page = int(page)

            start = request.GET.get("start")
            if start is None:
                start = ""

            if not (isinstance(page, int)):
                raise ValueError
            if not (isinstance(start, str)):
                raise ValueError

        except (KeyError, ValueError):
            return Response(error_response)

        music = Music.objects.get_many_music(start)[
            20 * page : 20 * (page + 1)
        ]
        return Response(MusicSerializer(music, many=True).data)
