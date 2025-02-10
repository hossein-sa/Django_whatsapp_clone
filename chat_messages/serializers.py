from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    sender_name = serializers.CharField(source='sender.email', read_only=True)

    class Meta:
        model = Message
        fields = ['id', 'chat', 'sender', 'content', 'message_type', 'state', 'media_file', 'created_at', 'sender_name']
