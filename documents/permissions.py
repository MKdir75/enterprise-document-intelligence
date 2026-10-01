from rest_framework.permissions import BasePermission


class CanCreateDocument(BasePermission):

    message = (
        "Only Admin, Manager, or Analyst "
        "can create documents."
    )

    def has_permission(
        self,
        request,
        view,
    ):
        return (
            request.user.is_authenticated
            and request.user.role
            in {
                "ADMIN",
                "MANAGER",
                "ANALYST",
            }
        )


class CanManageDocument(BasePermission):

    message = (
        "You do not have permission "
        "to manage this document."
    )

    def has_object_permission(
        self,
        request,
        view,
        obj,
    ):
        if not request.user.is_authenticated:
            return False

        if request.user.role == "ADMIN":
            return True

        if request.user.role == "MANAGER":
            return (
                obj.department_id
                == request.user.department_id
            )

        if request.user.role == "ANALYST":
            return (
                obj.department_id
                == request.user.department_id
                and obj.uploaded_by_id
                == request.user.id
            )

        return False