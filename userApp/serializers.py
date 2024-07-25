from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone_number', 'first_name', 'last_name', 'birth_date')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
