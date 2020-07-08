
from rest_framework import generics, mixins, permissions, status

from ..models import Info
from .permissions import DOorSA
from .serializers import (RegistrationSerializer, UserInfoGetSerializer,
                          UserInfoSerializer)


class Registeration(mixins.CreateModelMixin, generics.GenericAPIView):
       
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserInfoListView(generics.ListAPIView):
    serializer_class = UserInfoGetSerializer
    
    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Info.objects.all()
        elif user.info.role=='DO':
            return Info.objects.filter(organization=user.info.organization, role='EO')
    

class UserInfoDetailView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    
    # TODO: costom permission
    permission_classes = [permissions.IsAuthenticated, DOorSA]
    lookup_field = 'pk'
    serializer_class = UserInfoSerializer
    # queryset = Info.objects.all()
    
    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Info.objects.all()
        elif user.info.role=='DO':
            return Info.objects.filter(organization=user.info.organization, role='EO')
        

    def get_serializer_context(self):
        context = super(UserInfoDetailView, self).get_serializer_context()
        context.update({"request":self.request})
        return context


    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
