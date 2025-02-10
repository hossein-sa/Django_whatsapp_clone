from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Q
from users.models import User
from .models import Chat
from .serializers import ChatSerializer


# ✅ Create a new chat between two users
class ChatCreateView(generics.CreateAPIView):
    serializer_class = ChatSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        sender = self.request.user
        recipient_id = self.request.data.get('recipient')  # Expecting recipient ID

        try:
            recipient = User.objects.get(id=recipient_id)
        except User.DoesNotExist:
            return Response({"error": "Recipient does not exist"}, status=400)

        serializer.save(sender=sender, recipient=recipient)

# ✅ List all chats where the logged-in user is involved
class ChatListView(generics.ListAPIView):
    serializer_class = ChatSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Chat.objects.filter(Q(sender=user) | Q(recipient=user))
