import base64

from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import NewUser, UserNewFields
from users.serializers import UserProfileSerializer, UsersSerializer


error_response = {
    "success": False,
    "description": ["Ты отправил мне какую-то дичь"],
}


class DetailAPI(APIView):
    def get(self, request, pk, *args, **kwargs):
        user = User.objects.get(pk=pk)
        return Response(UserProfileSerializer(user).data)


class UsersAPI(APIView):
    def get(self, request, *args, **kwargs):
        page = request.GET.get("page")
        start = request.GET.get("start")

        if page is None:
            page = 0
        else:
            page = int(page)

        if start is None:
            start = ""

        users = NewUser.objects.get_users(start)[20 * page : 20 * (page + 1)]
        return Response(UsersSerializer(users, many=True).data)


class UsersChangeImageAPI(APIView):  # хуйня
    def post(self, request, *args, **kwargs):
        try:
            user_id = request.data["id"]
            image = request.data["image"]

            user = User.objects.get(pk=user_id)
        except (User.DoesNotExist, KeyError):
            return Response(error_response)

        new_fields = UserNewFields.objects.get(user=user)
        music = new_fields.music

        image_data_decoded = base64.b64decode(image)

        new_fields.delete()

        UserNewFields.objects.create(
            user=user,
            image=ContentFile(
                image_data_decoded,
                name=f"user_{user.id}_image.jpg",
            ),
            music=music,
        )

        return Response(
            {
                "success": True,
                "description": ["Изображение изменено!"],
            },
        )
