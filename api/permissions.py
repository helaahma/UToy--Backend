from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
	message = "You must be the owner of this booking"

	def has_object_permission(self, request, view, obj):
		if request.user.is_staff or (obj.user == request.user):
			return True
		else:
			return False
