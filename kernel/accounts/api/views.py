
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions

from .serializers import RegistrationSerializer, UserInfoSerializer
from ..models import Info

class Registeration(mixins.CreateModelMixin, generics.GenericAPIView):
       
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserInfoDetailView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    
    # TODO: costom permission
    permission_classes = [permissions.IsAuthenticated]
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