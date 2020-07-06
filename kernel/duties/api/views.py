from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions

from .serializers import EODutySerializer, DODutyCreationSerializer, DutyUpdateSerializer
from ..models import Duty
from .permissions import NotSiteAdmin, NotEE
from accounts.models import Info


class DutyView(mixins.CreateModelMixin, mixins.ListModelMixin, generics.GenericAPIView):

    permission_classes = [permissions.IsAuthenticated, NotSiteAdmin, NotEE]
    queryset = Duty.objects.all()


    def get_serializer_class(self):
        if self.request.user.is_staff:
            return DODutyCreationSerializer
        elif self.request.user.info.role=='EO':
            return EODutySerializer
        return DODutyCreationSerializer


    def get_serializer_context(self):
        context = super(DutyView, self).get_serializer_context()
        context.update({"request":self.request})
        return context

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Duty.objects.all()
        elif user.info.role=='DO':
            return Duty.objects.filter(usersinfo__in=list(Info.objects.filter(organization=user.info.organization))).distinct()
        elif user.info.role=='EO':
            return Duty.objects.filter(usersinfo__in=[user.info])

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



class DutyDetailView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    
    
    permission_classes = [permissions.IsAuthenticated, NotEE]
    lookup_field = 'pk'
    
    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Duty.objects.all()
        elif user.info.role=='DO':
            return Duty.objects.filter(usersinfo__in=list(Info.objects.filter(organization=user.info.organization))).distinct()
        elif user.info.role=='EO':
            return Duty.objects.filter(created_by=user)

    def get_serializer_context(self):
        context = super(DutyDetailView, self).get_serializer_context()
        context.update({"request":self.request})
        return context


    def get_serializer_class(self):
        if self.request.user.is_staff or self.request.user.info.role=="DO":
            return DutyUpdateSerializer
        return EODutySerializer


    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
        

