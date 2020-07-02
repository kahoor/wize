from rest_framework import serializers
from ..models import Organization, UpgradeRequest

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['name']


class UpgradeRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpgradeRequest
        fields = ['user', 'current_role', 'dream_role', 'organization', 'status', 'created']
        extra_kwargs = {
                'user': {'read_only': True},
                'current_role': {'read_only': True},
                'status': {'read_only': True},
                'created': {'read_only': True},
        }

    
    def save(self):

        upgraderequest = UpgradeRequest(
					user=self.context['request'].user,
                    current_role=self.context['request'].user.info.role,
                    organization=self.validated_data['organization'],
                    dream_role=self.validated_data['dream_role']
        )

        upgraderequest.save()
        return upgraderequest