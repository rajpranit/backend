from .permissions import IsStaffEdittedPermision
from rest_framework import permissions

class StaffEditorPermissionMixin():
    permission_classes = [permissions.IsAdminUser ,IsStaffEdittedPermision ]
