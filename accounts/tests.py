from django.test import TestCase

from .models import User


class UserModelTest(TestCase):

    def test_user_role_default(self):
        user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="StrongPassword123",
        )

        self.assertEqual(
            user.role,
            User.Role.USER,
        )
