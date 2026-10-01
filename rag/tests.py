from django.test import TestCase

from accounts.models import User

from .models import RAGQuery


class RAGQueryTest(TestCase):

    def test_rag_query_creation(self):
        user = User.objects.create_user(
            username="raguser",
            email="rag@example.com",
            password="StrongPassword123",
        )

        query = RAGQuery.objects.create(
            user=user,
            question="What is AI?",
            answer="AI is artificial intelligence.",
        )

        self.assertEqual(
            query.user,
            user,
        )

        self.assertEqual(
            query.question,
            "What is AI?",
        )