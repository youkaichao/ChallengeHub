from django.db import models
from django.utils import timezone
from useraction.models import User
from basic.models import Group, Competition
from typing import Dict, Any
# Create your models here.


class InvitationStatus:
    DEFAULT = 0
    ACCEPTED = 1
    REJECTED = 2
    CANCELLED = 3

    
class MessageType:
    letter = 'letter'
    invitation = 'invitation'
    reviewer_invitation = 'reviewer_invitation'
    system = 'system'
    

class Message(models.Model):
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField(blank=False)
    send_time = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)

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
        }
        return data

        
class SystemMessage(models.Model):
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='received_system_messages')
    content = models.TextField(blank=False)
    send_time = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'to {self.receiver.username}: {self.content}'

    def to_dict(self, detail: bool = False) -> Dict[str, Any]:
        data = {
            'id': self.id,
            'receiver': self.receiver.username,
            'sender': 'system',
            'content': self.content,
            'isRead': self.is_read,
            'sendTime': self.send_time.strftime('%Y-%m-%d'),
        }
        return data
        

class Invitation(models.Model):
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, related_name="sent_invitations")
    invitee = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="received_invitations")
    send_time = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)
    status = models.IntegerField(default=InvitationStatus.DEFAULT)

    def to_dict(self, detail: bool = False) -> Dict[str, Any]:
        data = {
            'id': self.id,
            'sender': self.group.leader.username,
            'receiver': self.invitee.username,
            'isRead': self.is_read,
            'sendTime': self.send_time.strftime('%Y-%m-%d')
        }
        return data

        
class ReviewerInvitation(models.Model):
    competition = models.ForeignKey(
        Competition, on_delete=models.CASCADE, related_name="sent_invitations")
    invitee = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="received_reviewer_invitations")
    send_time = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)
    status = models.IntegerField(default=InvitationStatus.DEFAULT)

    def to_dict(self, detail: bool = False) -> Dict[str, Any]:
        data = {
            'id': self.id,
            'sender': self.competition.publisher.username,
            'receiver': self.invitee.username,
            'isRead': self.is_read,
            'sendTime': self.send_time.strftime('%Y-%m-%d')
        }
        return data