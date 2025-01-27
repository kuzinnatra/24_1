from rest_framework.permissions import BasePermission


class IsModer(BasePermission):
    """Проверяет является ли пользователь администратором"""
    def has_permission(self, request, view):
        return request.user.groups.filter(name="moders").exists()


class IsOwner(BasePermission):
    """Проверяет является ли пользователь владельцем"""
    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False