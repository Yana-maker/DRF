from rest_framework.permissions import BasePermission

from users.models import UserRole


class IsOwner(BasePermission):
    massage = 'Вы не являетесь владельцем!'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
        return False


class IsModerator(BasePermission):
    massage = 'Вы не являетесь модератором!'

    def has_permission(self, request, view):
        if request.user.role == UserRole.MODERATOR:
            return True
        return False


class IsOwnerIsNotModerator(BasePermission):
    massage = 'Вы не являетесь владельцем!'

    def has_permission(self, request, view):
        if request.user.role != UserRole.MODERATOR and request.user.owner:
            return True
        return False


class IsNotModerator(BasePermission):
    massage = 'Вы модератор!'

    def has_permission(self, request, view):
        if request.user.role != UserRole.MODERATOR:
            return True
        return False