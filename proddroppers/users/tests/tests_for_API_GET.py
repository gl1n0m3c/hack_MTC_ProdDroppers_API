from django.test import Client, TestCase
from django.urls import reverse
import parameterized


error_description = ["Ты отправил мне какую-то дичь"]


class UsersTestsAPIGET(TestCase):
    fixtures = [
        "fixtures/test_users.json",
    ]

    @parameterized.parameterized.expand(
        [
            (
                {"page": 0, "start": ""},
                5,
                (
                    "Nick",
                    "test1",
                    "test2",
                    "test3",
                    "test4",
                ),
                (1, 2, 3, 4, 5),
            ),
            (
                {"page": 1, "start": ""},
                0,
                (),
                (),
            ),
            (
                {"page": 0, "start": "test"},
                4,
                (
                    "test1",
                    "test2",
                    "test3",
                    "test4",
                ),
                (2, 3, 4, 5),
            ),
        ],
    )
    def test_users_list_endpoint_success(
        self,
        params,
        number_of_friends,
        nicks,
        ids,
    ):
        response = Client().get(reverse("users:users"), params)

        answer = response.json()

        self.assertEqual(len(answer), number_of_friends)

        for n, friend in enumerate(answer):
            self.assertEqual(friend["user_id"], ids[n])
            self.assertEqual(friend["username"], nicks[n])
            self.assertEqual(friend["image"], None)

    @parameterized.parameterized.expand(
        [
            ({"page": "asd", "start": ""},),
            ({"page": True, "start": ""},),
            ({"page": "none", "start": ""},),
        ],
    )
    def test_users_list_endpoint_invalid(self, params):
        response = Client().get(reverse("users:users"), params)

        answer = response.data

        self.assertEqual(answer["success"], False)
        self.assertEqual(answer["description"], error_description)

    @parameterized.parameterized.expand(
        [
            (1, "Nick"),
            (2, "test1"),
            (3, "test2"),
            (4, "test3"),
            (5, "test4"),
        ],
    )
    def test_detail_endpoint_success(self, num, name):
        response = Client().get(reverse("users:profile", kwargs={"pk": num}))

        answer = response.data

        self.assertEqual(answer["id"], num)
        self.assertEqual(answer["username"], name)
        self.assertEqual(answer["email"], "")

    def test_detail_endpoint_invalid(self):
        response = Client().get(reverse("users:profile", kwargs={"pk": 6}))

        answer = response.data

        self.assertEqual(answer["success"], False)
