from django.db import models
from chats.models import Chat
from users.models import User
import uuid

class Message(models.Model):
    MESSAGE_TYPES = (
        ('TEXT', 'Text'),
        ('IMAGE', 'Image'),
        ('VIDEO', 'Video'),
        ('AUDIO', 'Audio'),
    )

    MESSAGE_STATES = (
        ('SENT', 'Sent'),
        ('SEEN', 'Seen'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    chat = models.ForeignKey(Chat, related_name="messages", on_delete=models.CASCADE)
    sender = models.ForeignKey(User, related_name="sent_messages", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="received_messages", on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    message_type = models.CharField(max_length=10, choices=MESSAGE_TYPES, default='TEXT')
    state = models.CharField(max_length=10, choices=MESSAGE_STATES, default='SENT')
    media_file = models.FileField(upload_to="uploads/messages/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender.email} to {self.receiver.email}"
