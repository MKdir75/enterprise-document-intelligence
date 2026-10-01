from django.test import TestCase

from accounts.models import User

from .models import Conversation


class ConversationTest(TestCase):

    def test_conversation_creation(self):
        user = User.objects.create_user(
            username="conversationuser",
            email="conversation@example.com",
            password="StrongPassword123",
        )

        conversation = Conversation.objects.create(
            user=user,
            title="AI Research",
        )

        self.assertEqual(
            conversation.user,
            user,
        )

        self.assertEqual(
            conversation.title,
            "AI Research",
        )