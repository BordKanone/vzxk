from rest_framework.permissions import BasePermission


class IsCustomerOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.customer == request.user
