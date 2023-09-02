from rest_framework.permissions import BasePermission

class IsAdminPermision(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff
    
class IsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated
    
    