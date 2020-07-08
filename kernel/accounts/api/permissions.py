from rest_framework.permissions import BasePermission


class DOorSA(BasePermission):
    """
    Allows access only to "DO or SA" users.
    """
    def has_permission(self, request, view):
        if request.user.is_staff or request.user.info.role=='DO':
            return True
        return False

