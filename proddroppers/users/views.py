from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView


from users.serializers import UserProfileSerializer


class DetailAPI(APIView):
    def get(self, request, pk, *args, **kwargs):
        user = User.objects.get(pk=pk)
        return Response(UserProfileSerializer(user).data)
