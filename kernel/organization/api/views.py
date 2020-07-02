from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions

from .serializers import OrganizationSerializer, UpgradeRequestSerializer

class OrganizationView(mixins.CreateModelMixin, generics.GenericAPIView):
       
    serializer_class = OrganizationSerializer
    permission_classes = [permissions.IsAdminUser]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class UpgradeRequestView(mixins.CreateModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView):
       
    serializer_class = UpgradeRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_context(self):
        context = super(UpgradeRequestView, self).get_serializer_context()
        context.update({"request":self.request})
        return context

    # def get_queryset(self):
    #     user = self.request.user
        
        

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
