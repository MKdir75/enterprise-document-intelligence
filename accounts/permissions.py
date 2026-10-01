from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):

    message = "Admin access is required."

    def has_permission(
        self,
        request,
        view,
    ):
        return (
            request.user.is_authenticated
            and request.user.role == "ADMIN"
        )


class IsAdminOrManager(BasePermission):

    message = (
        "Admin or Manager access is required."
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
            }
        )


class IsAdminManagerOrAnalyst(BasePermission):

    message = (
        "Admin, Manager, or Analyst access "
        "is required."
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


class IsStaffRole(BasePermission):

    message = (
        "Staff role access is required."
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


class IsOwnerOrAdmin(BasePermission):

    message = (
        "You do not have permission "
        "to access this resource."
    )

    def has_object_permission(
        self,
        request,
        view,
        obj,
    ):
        if (
            request.user.is_authenticated
            and request.user.role == "ADMIN"
        ):
            return True

        return obj == request.user