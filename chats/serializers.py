from rest_framework import serializers
from .models import Chat

class ChatSerializer(serializers.ModelSerializer):
    sender_name = serializers.CharField(source='sender.email', read_only=True)
    recipient_name = serializers.CharField(source='recipient.email', read_only=True)

    class Meta:
        model = Chat
        fields = ['id', 'recipient', 'created_at', 'sender_name', 'recipient_name']  # 👈 Removed 'sender'
