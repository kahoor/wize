
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics

from .serializers import RegistrationSerializer

class Registeration(mixins.CreateModelMixin, generics.GenericAPIView):
       
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
