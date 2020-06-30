from django.contrib.auth.models import User
from rest_framework import serializers
from ..models import Info


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password2']
        extra_kwargs = {
				'password': {'write_only': True,
                'style':{'input_type': 'password'}},
		}
    
    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
        	raise serializers.ValidationError({'password': 'Passwords must match.'})
        user = User(
					email=self.validated_data['email'],
					username=self.validated_data['username'],
                    password=password
        )
        user.save()
        info = Info()
        info.user = user
        info.save()

        return user
