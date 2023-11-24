import base64
import io

from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from PIL import Image
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import NewUser, UserNewFields
from users.serializers import UserProfileSerializer, UsersSerializer


error_response = {
    "success": False,
    "description": ["Ты отправил мне какую-то дичь"],
}


class UsersAPI(APIView):
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

        users = NewUser.objects.get_users(start)[20 * page : 20 * (page + 1)]
        return Response(UsersSerializer(users, many=True).data)


class DetailAPI(APIView):
    def get(self, request, pk, *args, **kwargs):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(error_response)
        return Response(UserProfileSerializer(user).data)


class UsersChangeImageAPI(APIView):
    def post(self, request, *args, **kwargs):
        try:
            user_id = request.data["id"]
            byte_data = request.data["image"]

            user = User.objects.get(pk=user_id)

            new_fields = UserNewFields.objects.get(user=user)
        except (User.DoesNotExist, KeyError):
            return Response(error_response)

        decoded_image = base64.b64decode(byte_data)
        image = Image.open(io.BytesIO(decoded_image))

        filename = f"user_{user.id}_image.{image.format.lower()}"

        if new_fields.image:
            new_fields.image.delete()

        new_fields.image.save(filename, ContentFile(decoded_image), save=True)
        new_fields.save()

        return Response(
            {
                "success": True,
                "description": ["Изображение изменено!"],
            },
        )
