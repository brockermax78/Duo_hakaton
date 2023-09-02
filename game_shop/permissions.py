from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS or request.user.is_staff:
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        if request.method == ['DELETE', 'PUT', 'PATCH', 'POST']:
            return request.user.is_staff
        return True    

class IsAdminOrPermissionIsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (request.user.is_active or request.user.is_staff)
    
class IsAuthorPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.author