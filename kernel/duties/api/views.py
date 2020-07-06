from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions

from .serializers import DutySerializer
from ..models import Duty


class DutyView(mixins.CreateModelMixin, mixins.ListModelMixin, generics.GenericAPIView):
       
    serializer_class = DutySerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Duty.objects.all()

    def get_serializer_context(self):
        context = super(DutyView, self).get_serializer_context()
        context.update({"request":self.request})
        return context

    # def get_queryset(self):
    #     user = self.request.user
    #     if user.is_superuser:
    #         return Duty.objects.all()
    #     elif user.info.role=='DO':
    #         return Duty.objects.filter()
    #     elif user.info.role in ['EE', 'EO']:
    #         return UpgradeRequest.objects.filter(user=user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



class DutyDetailView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    
    serializer_class = DutySerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'
    queryset = Duty.objects.all()

    # def get_queryset(self):
    #     user = self.request.user
    #     if user.is_superuser:
    #         return UpgradeRequest.objects.filter(current_role='EE', dream_role='DO')
    #     elif user.info.role=='DO':
    #         return UpgradeRequest.objects.filter(organization=user.info.organization)
    #     elif user.info.role in ['EE', 'EO']:
    #         return UpgradeRequest.objects.filter(user=user)

    def get_serializer_context(self):
        context = super(DutyDetailView, self).get_serializer_context()
        context.update({"request":self.request})
        return context


    # def get_serializer_class(self):
    #     if self.request.user.is_staff or self.request.user.info.role=="DO":
    #         return ChekUpgradeRequestSerializer
    #     return UpgradeRequestSerializer


    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
        

