from rest_framework import serializers
from ..models import Organization, UpgradeRequest

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['name']


class UpgradeRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpgradeRequest
        fields = ['dream_role', 'organization']

    def save(self):
        # dream_role = self.validated_data.pop('dream_role')
        # if not str(dream_role) in ['CO', 'EO']:
        #     raise serializers.ValidationError({'Dream role': 'Dream role can be CO or EO.'})
        
        upgraderequest = UpgradeRequest(
					user=self.context['request'].user,
                    current_role=self.context['request'].user.info.role,
                    organization=self.validated_data['organization'],
                    dream_role=self.validated_data['dream_role']
        )

        upgraderequest.save()
        return upgraderequest