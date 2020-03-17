from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    message = 'Вы должны быть владельцем этого теста'

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsTeacher(permissions.BasePermission):
    message = 'Вы должны быть учителем'

    def has_permission(self, request, view):
        return request.user.role == 'TE'
