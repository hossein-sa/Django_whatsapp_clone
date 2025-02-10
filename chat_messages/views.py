from rest_framework import generics
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from chats.models import Chat
from .models import Message
from .serializers import MessageSerializer


# ✅ Create a new message in an existing chat
class MessageCreateView(generics.CreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        chat = serializer.validated_data['chat']
        sender = self.request.user

        # Ensure the sender is part of the chat
        if sender not in [chat.sender, chat.recipient]:
            raise PermissionDenied("You are not a participant of this chat.")

        serializer.save(sender=sender)


# ✅ Get all messages from a chat
class MessageListView(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        chat_id = self.kwargs['chat_id']
        user = self.request.user

        try:
            chat = Chat.objects.get(id=chat_id)
            if user != chat.sender and user != chat.recipient:
                return Message.objects.none()
        except Chat.DoesNotExist:
            return Message.objects.none()

        return Message.objects.filter(chat=chat).order_by('created_at')
