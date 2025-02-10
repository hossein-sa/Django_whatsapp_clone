from django.db import models
from users.models import User
import uuid

class Chat(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chats_as_sender')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chats_as_recipient')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['sender', 'recipient'], name='unique_chat_between_users')
        ]

    def __str__(self):
        return f"Chat between {self.sender.email} and {self.recipient.email}"
