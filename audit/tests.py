from django.test import TestCase

from accounts.models import User

from .models import AuditLog


class AuditLogTest(TestCase):

    def test_audit_log_creation(self):
        user = User.objects.create_user(
            username="audituser",
            email="audit@example.com",
            password="StrongPassword123",
        )

        log = AuditLog.objects.create(
            user=user,
            action=AuditLog.Action.LOGIN,
            resource_type="AUTH",
            description="User logged in.",
        )

        self.assertEqual(
            log.user,
            user,
        )

        self.assertEqual(
            log.action,
            AuditLog.Action.LOGIN,
        )