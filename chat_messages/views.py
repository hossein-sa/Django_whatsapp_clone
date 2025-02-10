from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Message
from .serializers import MessageSerializer

# View for sending a message
class MessageCreateView(generics.CreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Get the sender and receiver from the request and save the message
        serializer.save(sender=self.request.user, receiver=self.request.data['receiver'])

# View to get messages by chat
class MessageListView(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Get the chat_id from the URL and retrieve all messages related to that chat
        chat_id = self.kwargs['chat_id']
        return Message.objects.filter(chat__id=chat_id).order_by('created_at')
