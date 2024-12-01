from rest_framework.permissions import BasePermission

class IsSuperUserOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        # Allow read-only access for any authenticated user
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return request.user.is_authenticated

        # Only superusers can perform write operations
        return request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        # Normal users can only view their own assignments
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return obj.assignee == request.user

        # Write operations are restricted to superusers
        return request.user.is_superuser
