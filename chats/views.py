from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Chat
from .serializers import ChatSerializer

# View to create a new chat between two users
class ChatCreateView(generics.CreateAPIView):
    serializer_class = ChatSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically set the sender from the logged-in user
        serializer.save(sender=self.request.user)

# View to list all chats for the logged-in user
class ChatListView(generics.ListAPIView):
    serializer_class = ChatSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Retrieve all chats where the user is either the sender or recipient
        user = self.request.user
        return Chat.objects.filter(sender=user) | Chat.objects.filter(recipient=user)
