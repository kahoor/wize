from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions

from .serializers import OrganizationSerializer, UpgradeRequestSerializer, ChekUpgradeRequestSerializer
from ..models import UpgradeRequest

class OrganizationView(mixins.CreateModelMixin, generics.GenericAPIView):
       
    serializer_class = OrganizationSerializer
    permission_classes = [permissions.IsAdminUser]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class UpgradeRequestView(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView):
       
    serializer_class = UpgradeRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_context(self):
        context = super(UpgradeRequestView, self).get_serializer_context()
        context.update({"request":self.request})
        return context

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return UpgradeRequest.objects.filter(current_role='EE', dream_role='DO')
        elif user.info.role=='DO':
            return UpgradeRequest.objects.filter(organization=user.info.organization)
        elif user.info.role in ['EE', 'EO']:
            return UpgradeRequest.objects.filter(user=user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class UpgradeRequestDetailView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'
    
    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return UpgradeRequest.objects.filter(current_role='EE', dream_role='DO')
        elif user.info.role=='DO':
            return UpgradeRequest.objects.filter(organization=user.info.organization)
        elif user.info.role in ['EE', 'EO']:
            return UpgradeRequest.objects.filter(user=user)

    def get_serializer_context(self):
        context = super(UpgradeRequestDetailView, self).get_serializer_context()
        context.update({"request":self.request})
        return context


    def get_serializer_class(self):
        if self.request.user.is_staff or self.request.user.info.role=="DO":
            return ChekUpgradeRequestSerializer
        return UpgradeRequestSerializer


    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
        
