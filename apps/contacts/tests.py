from rest_framework.reverse import reverse, reverse_lazy
from rest_framework.test import APITestCase
from apps.accounts.models import User
from apps.contacts.models import Contact


class UserMixin(object):
    @staticmethod
    def _create_user(user_number: int):
        user = User.objects.create(
            email=f"test{user_number}@example.com",
        )
        user.set_password(f"testPassword")
        user.save()
        return user


class ContactTestCase(APITestCase, UserMixin):
    def setUp(self) -> None:
        self.user_1 = self._create_user(user_number=1)
        self.user_2 = self._create_user(user_number=2)
        self.user_3 = self._create_user(user_number=3)

        self.login_url = reverse("super_login")
        self.contact_list_url = reverse("contacts:contact-list")
        self.contact_detail_url = reverse("contacts:contact-detail", kwargs={"pk": 1})

        self.contact = Contact.objects.create(
            first_name="Aleks", last_name="Sparrow", phone="+380938162416", user=self.user_1
        )

    def _get_user_token(self, email="test1@example.com", password="testPassword"):
        response = self.client.post(
            self.login_url,
            {"username": email, "password": password},
            format="json",
        )
        response_data = response.json()
        return "JWT {}".format(response_data.get("token", ""))

    def test_create_contact(self):
        # Contact creation test
        result = self.client.post(
            self.contact_list_url,
            {"first_name": "Aleks", "last_name": "Sparrow", "phone": "+380938162416", "user":1},
            HTTP_AUTHORIZATION=self._get_user_token(email=self.user_1.email),
        )
        self.assertEqual(result.status_code, 201)
