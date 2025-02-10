from django.db import models
from users.models import User
import uuid

class Chat(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender = models.ForeignKey(User, related_name="chats_as_sender", on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name="chats_as_recipient", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat between {self.sender.email} and {self.recipient.email}"
