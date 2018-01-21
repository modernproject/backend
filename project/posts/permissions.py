from rest_framework import permissions

class IsAvailableArticle(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            if request.user and request.user.is_staff:
                return True
            elif obj.premium and not request.user.is_anonymous and request.user.valid_subscription():
                return True
            elif obj.premium == False:
                return True
        else:
            return False