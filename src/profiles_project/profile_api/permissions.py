from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    #Allows user to update their own profile

    def has_object_permission(self, request, view, obj):
        #Check if useer has the permission to edit its profile

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id