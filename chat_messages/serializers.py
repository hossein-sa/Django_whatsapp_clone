from rest_framework import serializers
from .models import Message
from chats.models import Chat
from users.models import User

class MessageSerializer(serializers.ModelSerializer):
    sender_name = serializers.CharField(source='sender.email', read_only=True)
    receiver_name = serializers.CharField(source='receiver.email', read_only=True)

    class Meta:
        model = Message
        fields = ['id', 'chat', 'sender', 'receiver', 'content', 'message_type', 'state', 'media_file', 'created_at', 'sender_name', 'receiver_name']
