from rest_framework import serializers
from .models import SuperMc

class SuperMcSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperMc
        fields = ['id', 'username', 'phone' ,'key']

class SuperMcContactListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperMc
        fields = ['phone']

# CustomerData

class SuperMcVerifyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperMc
        fields = ['phone', 'key']

class SuperMcResetKey(serializers.ModelSerializer):
    class Meta:
        model = SuperMc
        fields = ['phone', 'key']