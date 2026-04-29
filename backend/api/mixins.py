from .permissions import IsStaffEditorPermission
from rest_framework import generics, permissions, authentication, mixins
class StaffEditorPermissionMixin:
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]