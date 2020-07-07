from rest_framework import serializers

from ..models import Organization, UpgradeRequest


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['name']


class UpgradeRequestSerializer(serializers.ModelSerializer):
    my_absolute_url = serializers.URLField(source='get_absolute_url', read_only=True) 
    class Meta:
        model = UpgradeRequest
        fields = ['id', 'user', 'current_role', 'dream_role', 'organization', 'status', 'created', 'my_absolute_url']
        read_only_fields = ['user', 'current_role', 'status', 'created']

    
    def save(self):

        upgraderequest = UpgradeRequest(
					user=self.context['request'].user,
                    current_role=self.context['request'].user.info.role,
                    organization=self.validated_data['organization'],
                    dream_role=self.validated_data['dream_role']
        )

        upgraderequest.save()
        return upgraderequest

class ChekUpgradeRequestSerializer(serializers.ModelSerializer):
    my_absolute_url = serializers.URLField(source='get_absolute_url', read_only=True) 
    class Meta:
        model = UpgradeRequest
        fields = ['id', 'user', 'current_role', 'dream_role', 'organization', 'status', 'created', 'my_absolute_url']
        read_only_fields = ['user', 'current_role', 'dream_role', 'organization', 'created']

    def save(self):
        self.instance.status = self.validated_data['status']
        if self.validated_data['status']=='ACC':
            if self.instance.dream_role=='DO':
                self.instance.user.info.make_DO(self.instance.organization)
            elif self.instance.dream_role=='EO':
                self.instance.user.info.make_EO(self.instance.organization)
        self.instance.user.info.save()
        self.instance.save()
        return self.instance
