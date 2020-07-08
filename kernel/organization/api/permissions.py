from rest_framework.permissions import BasePermission


class NotSiteAdmin(BasePermission):
    """
    Allows access "POST" only to "NotSiteAdmin" users.
    """
    def has_permission(self, request, view):
        if request.method=="POST":
            return not request.user.is_staff
        return True

class NotDO(BasePermission):
    """
    Allows access "POST" only to "NotDO" users.
    """
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True

        elif request.method=="POST":
            return not request.user.info.role == 'DO'
        
        return True
