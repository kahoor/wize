from rest_framework import serializers
from ..models import Duty
from accounts.models import Info

class EODutySerializer(serializers.ModelSerializer):
    my_absolute_url = serializers.URLField(source='get_absolute_url', read_only=True)
    deadline = serializers.DateTimeField(required=True)
    class Meta:
        model = Duty
        fields = [ 'id', 'created_by','usersinfo', 'title', 'describtion', 'created', 'deadline', 'my_absolute_url']
        read_only_fields = ['created', 'usersinfo', 'created_by']


    def save(self):
        request = self.context['request']
        user = request.user
        if request.method == 'POST':
            duty = Duty(
                        created_by = user,
                        title = self.validated_data['title'],
                        describtion = self.validated_data['describtion'],
                        deadline = self.validated_data['deadline'],
            )
            duty.save()
            duty.usersinfo.add(user.info)
            return self.instance

        elif request.method == 'PUT':
            duty = self.instance
            duty.title = self.validated_data['title']
            duty.describtion = self.validated_data['describtion']
            duty.deadline = self.validated_data['deadline']
            duty.save()    

        return duty        

class DODutyCreationSerializer(serializers.ModelSerializer):
    my_absolute_url = serializers.URLField(source='get_absolute_url', read_only=True)
    deadline = serializers.DateTimeField(required=True)
    class Meta:
        model = Duty
        fields = [ 'id', 'created_by', 'usersinfo', 'title', 'describtion', 'created', 'deadline', 'my_absolute_url']
        read_only_fields = ['created', 'created_by']


    def save(self):
        request = self.context['request']
        user = request.user
        usersinfo = self.validated_data['usersinfo']
        
        for i in usersinfo:
            
            if i.organization!=user.info.organization or i.role!='EO':
                raise serializers.ValidationError({'usersinfo':"You can't give {} a duty!".format(i)})
        
        duty = Duty(
                    created_by = user,
                    title = self.validated_data['title'],
                    describtion = self.validated_data['describtion'],
                    deadline = self.validated_data['deadline'],
        )
        duty.save()
        duty.usersinfo.set(usersinfo)
        return duty        

class DutyUpdateSerializer(serializers.ModelSerializer):
    my_absolute_url = serializers.URLField(source='get_absolute_url', read_only=True)
    deadline = serializers.DateTimeField(required=True)
    class Meta:
        model = Duty
        fields = [ 'id', 'created_by', 'usersinfo', 'title', 'describtion', 'created', 'deadline', 'my_absolute_url']
        read_only_fields = ['created', 'title', 'describtion', 'created_by',]


    def save(self):
        request = self.context['request']
        user = request.user
        usersinfo = self.validated_data['userinfo']

        if not user.is_staff:
            for i in usersinfo:
                t=Info.objects.get(pk=i)
                if t.organization!=user.info.organization or t.role!='EO':
                    raise serializers.ValidationError({'usersinfo':"You can't give {} a duty!".format(t)})
        
        duty = self.instance
        duty.deadline = self.validated_data['deadline']
        duty.usersinfo.set(usersinfo)
        duty.save()    
    
        return duty      



# class DutySerializer(serializers.ModelSerializer):
#     my_absolute_url = serializers.URLField(source='get_absolute_url', read_only=True)
#     deadline = serializers.DateTimeField(required=True)
#     class Meta:
#         model = Duty
#         fields = [ 'id', 'usersinfo', 'title', 'describtion', 'created', 'deadline', 'my_absolute_url']
#         read_only_fields = ['created',]

    
#     def save(self):
#         request = self.context['request']
#         user = request.user
#         if request.method == 'POST':
#             usersinfo = self.validated_data['usersinfo']
#             if user.info.role=='EO' and usersinfo:
#                 raise serializers.ValidationError({'role':'You have no such permission.'})
#             duty = Duty(
#                         title = self.validated_data['title'],
#                         describtion = self.validated_data['describtion'],
#                         deadline = self.validated_data['deadline'],
#             )

#             duty.save()
#             duty.usersinfo.set(self.validated_data['usersinfo'])

#         elif request.method == 'PUT':
#             duty = self.instance
#             duty.title = self.validated_data['title']
#             duty.describtion = self.validated_data['describtion']
#             duty.deadline = self.validated_data['deadline']
#             duty.usersinfo.set(self.validated_data['usersinfo'])
#             duty.save()    
        

#         return duty