from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _ 
from rest_framework import serializers
from .models import User, UserData

class UserSerializer(serializers.ModelSerializer):
    """Serializer for the users object"""

    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'name', "dateOfBirth", "phone_no", "height", "weight",)
        extra_kwargs = {'password': {'write_only':True, 'min_length':5}}

    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        return get_user_model().objects.create_user(**validated_data)  

    def create_superuser(self, validated_data):
        return get_user_model().objects.create_superuser(**validated_data)  

    def update(self, instance, validated_data):
        """Update a user, setting the password correctly and return it"""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


# class AdminUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = get_user_model()
#         fields = ('email', 'password','name', "dateOfBirth", "phone_no", "height", "weight",)
#         extra_kwargs = {'password': {'write_only':True, 'min_length':5}}
    
#     def create_superuser(self, validated_data):
#         return get_user_model().objects.create_superuser(**validated_data)  


class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user authentication  object"""
    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type':'password'}, 
        trim_whitespace = False
    )

    def validate(self, attrs):
        """Validate and authenticate the user"""
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request = self.context.get('request'),
            username = email,
            password = password
        )
        if not user:
            msg = _('Unable to authenticate with provided credentials')
            raise serializers.ValidationError(msg, code='authentication')

        attrs['user'] = user 
        return attrs  


class UserDataSerializer(serializers.ModelSerializer):
    """Serializing the User Data"""
    class Meta:
        model           = UserData
        fields          = ('id', 'steps', 'calories', 'points',)
        read_only_fields=('id',)


class UserLeaderBoardSerializer(serializers.ModelSerializer):
    """Serialzing all users points"""
    user_name = serializers.CharField(source='user.name')
    class Meta:
        model = UserData
        fields = ('id', 'user_name', 'points',)
        read_only_fields=('id',)
    