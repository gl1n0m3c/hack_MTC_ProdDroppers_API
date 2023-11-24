from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse
import parameterized

from users.models import UserNewFields
from users.tests.byte_files import byte_file_1, byte_file_2, byte_file_3


class UsersTestsAPIPOST(TestCase):
    fixtures = [
        "fixtures/test_users.json",
    ]

    @parameterized.parameterized.expand(
        [
            ({"id": 1, "image": byte_file_1.byte_data.decode("utf-8")},),
            ({"id": 1, "image": byte_file_2.byte_data.decode("utf-8")},),
            ({"id": 1, "image": byte_file_3.byte_data.decode("utf-8")},),
        ],
    )
    def test_users_change_image(self, params):
        response = Client().post(
            reverse("users:change_image"),
            data=params,
        )
        answer = response.json()

        self.assertEqual(answer["success"], True)
        self.assertEqual(answer["description"], ["Изображение изменено!"])

        user = User.objects.get(pk=1)
        new_fields = UserNewFields.objects.get(user=user)

        filename = new_fields.image.name.split("/")[-1]
        self.assertEqual(filename, "user_1_image.png")

        new_fields.image.delete()
        new_fields.save()
