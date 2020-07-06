from rest_framework.permissions import BasePermission


# Custom permission for users with "is_active" = True.
class NotSiteAdmin(BasePermission):
    """
    Allows access "POST" only to "NotSiteAdmin" users.
    """
    def has_permission(self, request, view):
        if request.method=="POST":
            return not request.user.is_staff
        return True

class NotEE(BasePermission):
    """
    Allows access only to "NotEE" users.
    """
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        return not request.user.info.role == 'EE'
