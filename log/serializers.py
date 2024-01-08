from rest_framework import serializers
from .models import SuperMc

class SuperMcSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperMc
        fields = ['id', 'username', 'phone', 'login_password', 'login_email' ,'key']

class SuperMcCheckRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperMc
        fields = ['phone', 'login_password', 'login_email']