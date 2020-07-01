from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions

from .serializers import OrganizationSerializer, UpgradeRequestSerializer

class OrganizationView(mixins.CreateModelMixin, generics.GenericAPIView):
       
    serializer_class = OrganizationSerializer
    permission_classes = [permissions.IsAdminUser]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class UpgradeRequestView(mixins.CreateModelMixin, generics.GenericAPIView):
       
    serializer_class = UpgradeRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)