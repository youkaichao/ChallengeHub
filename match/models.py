from django.db import models
from django.utils import timezone
from useraction.models import User
from typing import Dict, Any
# Create your models here.


class MessageType:
    DEFAULT = 0
    SYSTEM = 1
    INVITATION = 2


class InivationStatus:
    DEFAULT = 0
    ACCEPTED = 1
    REJECTED = 2
    CANCELLED = 3


class Message(models.Model):
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField(blank=False)
    send_time = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)
    category = models.IntegerField(default=MessageType.DEFAULT)
    status = models.IntegerField(default=InivationStatus.DEFAULT)

    def __str__(self) -> str:
        return f'to {self.receiver.username}: {self.content}'

    def to_dict(self, detail: bool = False) -> Dict[str, Any]:
        data = {
            'id': self.id,
            'receiver': self.receiver.username,
            'sender': self.sender.username,
            'content': self.content,
            'isRead': self.is_read,
            'sendTime': self.send_time.strftime('%Y-%m-%d'),
            'category': self.category,
            'status': self.status,
        }
        return data
