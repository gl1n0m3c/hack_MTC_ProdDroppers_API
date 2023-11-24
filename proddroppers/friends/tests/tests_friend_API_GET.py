from django.test import Client, TestCase
from django.urls import NoReverseMatch, reverse
import parameterized


class FriendsTestsAPIGET(TestCase):
    fixtures = [
        "fixtures/test_users.json",
        "fixtures/test_friends.json",
    ]

    @parameterized.parameterized.expand(
        [
            (1, 0, ()),
            (2, 2, ("test2", "test4")),
            (3, 1, ("test1",)),
            (4, 0, ()),
            (5, 1, ("test1",)),
            (6, 0, ()),
            (100, 0, ()),
        ],
    )
    def test_friends_list_endpoint_success(
        self,
        user_id,
        number_of_friends,
        nicks_of_friends,
    ):
        response = Client().get(
            reverse("friends:list", kwargs={"pk": user_id}),
        )

        answer = response.json()

        self.assertEqual(len(answer["data"]), number_of_friends)
        self.assertEqual(response.status_code, 200)

        for i in range(len(answer["data"])):
            self.assertEqual(
                answer["data"][i]["username"],
                nicks_of_friends[i],
            )

    @parameterized.parameterized.expand([True, "asd123", None])
    def test_friends_list_endpoint_invalid(
        self,
        user_id,
    ):
        with self.assertRaises(NoReverseMatch):
            Client().get(reverse("friends:list", kwargs={"pk": user_id}))

    @parameterized.parameterized.expand(
        [
            (1, 0, ()),
            (2, 1, ("test3",)),
            (3, 2, ("test3", "test4")),
            (4, 0, ()),
            (5, 0, ()),
            (6, 0, ()),
            (100, 0, ()),
        ],
    )
    def test_waiting_friends_list_endpoint_success(
        self,
        user_id,
        number_of_waiters,
        nicks_of_waiters,
    ):
        response = Client().get(
            reverse("friends:waiting", kwargs={"pk": user_id}),
        )

        answer = response.json()

        self.assertEqual(len(answer["data"]), number_of_waiters)
        self.assertEqual(response.status_code, 200)

        for i in range(len(answer["data"])):
            self.assertEqual(
                answer["data"][i]["username"],
                nicks_of_waiters[i],
            )

    @parameterized.parameterized.expand([True, "asd123", None])
    def test_waiting_friends_list_endpoint_invalid(
        self,
        user_id,
    ):
        with self.assertRaises(NoReverseMatch):
            Client().get(reverse("friends:waiting", kwargs={"pk": user_id}))
