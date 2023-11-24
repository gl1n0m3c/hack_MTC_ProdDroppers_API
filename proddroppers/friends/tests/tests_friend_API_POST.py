from django.test import Client, TestCase
from django.urls import reverse
import parameterized


error_description = ["Ты отправил мне какую-то дичь"]


class FriendsTestsAPIPOST(TestCase):
    fixtures = [
        "fixtures/test_users.json",
        "fixtures/test_friends.json",
    ]

    @parameterized.parameterized.expand(
        [
            ({"sender": 4, "receiver": 5},),
            ({"sender": 5, "receiver": 4},),
        ],
    )
    def test_add_friends_endpoint_success(
        self,
        params,
    ):
        response = Client().post(reverse("friends:add"), data=params)

        answer = response.json()

        self.assertEqual(answer["success"], True)
        self.assertEqual(
            answer["description"],
            ["Ваша заявка успешно отправлена!"],
        )

    @parameterized.parameterized.expand(
        [
            (
                {"sender": 4, "receiver": 3},
                ["Вы уже отправили заявку этому пользователю!"],
            ),
            (
                {"sender": 3, "receiver": 4},
                ["Этот пользователь уже отправил вам заявку!"],
            ),
            (
                {"sender": 2, "receiver": 3},
                ["Вы уже добавили этого пользователя в друзья!"],
            ),
            (
                {"sender": 0, "receiver": 0},
                error_description,
            ),
            (
                {"sender": "asd123", "receiver": "123"},
                error_description,
            ),
            (
                {"sender": True, "receiver": False},
                error_description,
            ),
        ],
    )
    def test_add_friends_endpoint_invalid(
        self,
        params,
        message,
    ):
        response = Client().post(reverse("friends:add"), data=params)

        answer = response.json()

        self.assertEqual(answer["success"], False)
        self.assertEqual(answer["description"], message)

    @parameterized.parameterized.expand(
        [
            ({"sender": 4, "receiver": 3},),
            ({"sender": 4, "receiver": 2},),
            ({"sender": 5, "receiver": 3},),
        ],
    )
    def test_assept_friends_endpoint_success(
        self,
        params,
    ):
        response = Client().post(reverse("friends:assept"), data=params)

        answer = response.json()

        self.assertEqual(answer["success"], True)
        self.assertEqual(answer["description"], ["Заявка принята!"])

    @parameterized.parameterized.expand(
        [
            (
                {"sender": 4, "receiver": 5},
                [
                    "Этот пользователь не отправлял вам запрос в друзья!",
                ],
            ),
            (
                {"sender": 5, "receiver": 4},
                [
                    "Этот пользователь не отправлял вам запрос в друзья!",
                ],
            ),
            (
                {"sender": 0, "receiver": 0},
                error_description,
            ),
            (
                {"sender": True, "receiver": False},
                error_description,
            ),
        ],
    )
    def test_assept_friends_endpoint_invalid(
        self,
        params,
        message,
    ):
        response = Client().post(reverse("friends:assept"), data=params)

        answer = response.json()

        self.assertEqual(answer["success"], False)
        self.assertEqual(answer["description"], message)

    @parameterized.parameterized.expand(
        [
            ({"sender": 4, "receiver": 3},),
            ({"sender": 4, "receiver": 2},),
            ({"sender": 5, "receiver": 3},),
        ],
    )
    def test_reject_friends_endpoint_success(
        self,
        params,
    ):
        response = Client().post(reverse("friends:reject"), data=params)

        answer = response.json()

        self.assertEqual(answer["success"], True)
        self.assertEqual(answer["description"], ["Заявка отклонена!"])

    @parameterized.parameterized.expand(
        [
            (
                {"sender": 4, "receiver": 5},
                [
                    "Этот пользователь не отправлял вам запрос в друзья!",
                ],
            ),
            (
                {"sender": 5, "receiver": 4},
                [
                    "Этот пользователь не отправлял вам запрос в друзья!",
                ],
            ),
            (
                {"sender": 0, "receiver": 0},
                error_description,
            ),
            (
                {"sender": True, "receiver": False},
                error_description,
            ),
        ],
    )
    def test_reject_friends_endpoint_invalid(
        self,
        params,
        message,
    ):
        response = Client().post(reverse("friends:reject"), data=params)

        answer = response.json()

        self.assertEqual(answer["success"], False)
        self.assertEqual(answer["description"], message)

    @parameterized.parameterized.expand(
        [
            ({"sender": 3, "receiver": 2},),
            ({"sender": 2, "receiver": 3},),
            ({"sender": 5, "receiver": 2},),
            ({"sender": 2, "receiver": 5},),
        ],
    )
    def test_delete_friends_endpoint_success(
        self,
        params,
    ):
        response = Client().post(reverse("friends:delete"), data=params)

        answer = response.json()

        self.assertEqual(answer["success"], True)
        self.assertEqual(answer["description"], ["Пользователь удален!"])

    @parameterized.parameterized.expand(
        [
            (
                {"sender": 4, "receiver": 5},
                ["Этот пользователь не является вашим другом!"],
            ),
            (
                {"sender": 5, "receiver": 4},
                ["Этот пользователь не является вашим другом!"],
            ),
            (
                {"sender": 0, "receiver": 0},
                error_description,
            ),
            (
                {"sender": True, "receiver": False},
                error_description,
            ),
        ],
    )
    def test_delete_friends_endpoint_invalid(
        self,
        params,
        message,
    ):
        response = Client().post(reverse("friends:delete"), data=params)

        answer = response.json()

        self.assertEqual(answer["success"], False)
        self.assertEqual(answer["description"], message)
