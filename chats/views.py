from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Q
from users.models import User
from .models import Chat
from .serializers import ChatSerializer
from rest_framework import status

# ✅ Create a new chat between two users
class ChatCreateView(generics.CreateAPIView):
    serializer_class = ChatSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        sender = self.request.user
        recipient_id = self.request.data.get('recipient')  # Expecting recipient ID

        # Validate recipient exists
        try:
            recipient = User.objects.get(id=recipient_id)
        except User.DoesNotExist:
            raise Response({"error": "Recipient does not exist"}, status=status.HTTP_400_BAD_REQUEST)

        # Prevent duplicate chats
        existing_chat = Chat.objects.filter(
            Q(sender=sender, recipient=recipient) | Q(sender=recipient, recipient=sender)
        ).first()

        if existing_chat:
            raise Response({"error": "Chat already exists"}, status=status.HTTP_400_BAD_REQUEST)

        # Save with sender auto-assigned
        serializer.save(sender=sender, recipient=recipient)

# ✅ List all chats where the logged-in user is involved
class ChatListView(generics.ListAPIView):
    serializer_class = ChatSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Chat.objects.filter(Q(sender=user) | Q(recipient=user))
