from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    #Allows user to update their own profile

    def has_object_permission(self, request, view, obj):
        #Check if useer has the permission to edit its profile

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id

class PostOwnStatus(permissions.BasePermission):
    #Allow users to update their own feed status

    def has_object_permission(self, request, view, obj):
        # Checks if user is trying to update its own status

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id 

