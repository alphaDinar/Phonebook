from rest_framework import serializers
from .models import SuperMc

class SuperMcSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperMc
        fields = ['id', 'username', 'phone', 'password', 'key']

class SuperMcCheckRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperMc
        fields = ['phone', 'password']