from rest_framework import serializers
from django.contrib.auth import get_user_model


class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['email', 'id', 'first_name', 'last_name']
        extra_kwargs = {'id': {'read_only': True}}




