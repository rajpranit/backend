from .permissions import IsStaffEdittedPermision
from rest_framework import permissions

class StaffEditorPermissionMixin():
    permission_classes = [permissions.IsAdminUser ,IsStaffEdittedPermision ]

class UserQuerySetMixin():
    user_field = "user"
    staff_lookup_view = False

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        lookup_data = {}
        lookup_data[self.user_field] = user
        qs = super().get_queryset(*args, **kwargs)
        if self.staff_lookup_view and user.is_staff:
            return qs
        return qs.filter(**lookup_data)
