from rest_framework import serializers

from .models import Profile, Operations

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['slackUsername', 'backend', 'age', 'bio']

class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operations
        fields = '__all__'