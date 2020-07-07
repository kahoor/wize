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
        user = User.objects.create_user(
					email=self.validated_data['email'],
					username=self.validated_data['username'],
                    password=password
        )
        user.save()
        info = Info()
        info.user = user
        info.save()

        return user


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ['user', 'role', 'organization']
        read_only_fields = ['user']

    def save(self):
        request = self.context['request']
        old_role = self.instance.role
        old_organization = self.instance.organization
        new_role = self.validated_data['role']
        new_organization = self.validated_data['organization']


        if request.user.is_superuser:
            if old_role=='EE' and new_role=="DO":
                raise serializers.ValidationError({'role':'You have no such permission.'})
            if old_role=='EE' and new_role=='EE' and new_organization!=old_organization:
                raise serializers.ValidationError({'role':'You have no such permission.'})
        
        elif request.user.info.role=='DO':
            if new_role=='DO' or new_organization!=old_organization:
                raise serializers.ValidationError({'role':'You have no such permission.'})
        
        if new_role=="EE":
            self.instance.user.info.make_EE()
        elif new_role=="EO":
            self.instance.user.info.make_EO(new_organization)
        elif new_role=="DO":
            self.instance.user.info.make_DO(new_organization)

        self.instance.user.info.save()
        self.instance.save()
        return self.instance
