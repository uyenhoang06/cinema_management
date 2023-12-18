from rest_framework import serializers
from .models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=100, min_length=8, write_only=True)
    password2 = serializers.CharField(max_length=100, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = [ 'first_name', 'last_name', 'email', 'phone', 'password', 'password2', 'address', 'gender']

    def validate(self, attrs):
        password = attrs.get('password', '')
        password2 = attrs.get('password2', '')
        if password != password2:
            raise serializers.ValidationError("password do not match")
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(
            first_name= validated_data.get('first_name'),
            last_name= validated_data.get('last_name'),
            email= validated_data.get('email'),
            phone=validated_data.get('phone'),
            password=validated_data.get('password'),
            address=validated_data.get('address'),
            gender=validated_data.get('gender')

        )
        return user
