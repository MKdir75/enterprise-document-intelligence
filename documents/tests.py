from django.test import TestCase

from accounts.models import User
from departments.models import Department

from .models import Document


class DocumentModelTest(TestCase):

    def setUp(self):
        self.department = Department.objects.create(
            name="Engineering",
            code="ENG",
        )

        self.user = User.objects.create_user(
            username="analyst",
            email="analyst@example.com",
            password="StrongPassword123",
            role=User.Role.ANALYST,
            department=self.department,
        )

    def test_document_creation(self):
        document = Document.objects.create(
            title="Engineering Policy",
            description="Test document.",
            document_type=Document.DocumentType.TXT,
            department=self.department,
            uploaded_by=self.user,
        )

        self.assertEqual(
            document.title,
            "Engineering Policy",
        )

        self.assertEqual(
            document.department,
            self.department,
        )