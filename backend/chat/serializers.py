from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import ChatModel


class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['email', 'id', 'first_name', 'last_name']
        extra_kwargs = {'id': {'read_only': True}}

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatModel
        fields = ['sender', 'message', 'reciever','time_stamp','id']
        extra_kwargs = {'time_stamp': {'read_only': True}}



