from rest_framework import serializers
from ..models import Duty

class DutySerializer(serializers.ModelSerializer):
    my_absolute_url = serializers.URLField(source='get_absolute_url', read_only=True)
    deadline = serializers.DateTimeField(required=True)
    class Meta:
        model = Duty
        fields = [ 'id', 'usersinfo', 'title', 'describtion', 'created', 'deadline', 'my_absolute_url']
        read_only_fields = ['created',]

    
    def save(self):

        if self.context['request'].method == 'POST':
            duty = Duty(
                        title = self.validated_data['title'],
                        describtion = self.validated_data['describtion'],
                        deadline = self.validated_data['deadline'],
            )

            duty.save()
            duty.usersinfo.set(self.validated_data['usersinfo'])
            return duty

        elif self.context['request'].method == 'PUT':
            
            self.instance.title = self.validated_data['title']
            self.instance.describtion = self.validated_data['describtion']
            self.instance.deadline = self.validated_data['deadline']
            self.instance.usersinfo.set(self.validated_data['usersinfo'])
            self.instance.save()    
            return self.instance
