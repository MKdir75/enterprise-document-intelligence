from django.test import TestCase

from .models import Department


class DepartmentModelTest(TestCase):

    def test_department_creation(self):
        department = Department.objects.create(
            name="Engineering",
            code="ENG",
            description=(
                "Engineering department."
            ),
        )

        self.assertEqual(
            department.name,
            "Engineering",
        )