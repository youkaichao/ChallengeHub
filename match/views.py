from django.shortcuts import render
from ChallengeHub.utils import BaseView as View, require_logged_in
from useraction.models import User
from match.models import Message, Invitation, InivationStatus
from basic.models import Competition, Group
from typing import Any
import json
# Create your views here.


class MatchGroupView(View):
    @require_logged_in
    def get(self, request, contest_id: str) -> Any:
        competition = Competition.objects.get(id=int(contest_id))
        groups = competition.enrolled_groups.all()
        if 'username' in request.data:
            leaderG = groups.filter(
                leader__username=request.data.get('username'))
            memberG = groups.filter(
                members__username=request.data.get('username'))
            groups = leaderG.union(memberG)

        if 'teamId' in request.data:
            groups = groups.filter(
                id=request.data.get('teamId'))
        return [{
            'teamId': group.id,
            'teamName': group.name,
            'leader': group.leader.username,
            'members': [member.username for member in group.members],
            'invitees': [i.invitee.username for i in Invitation.objects.filter(group=group)],
            'locked': group.locked,
        } for group in groups]


class MatchInviteView(View):
    @require_logged_in
    def post(self, request, contest_id: str, group_id: str)->Any:
        group = Group.objects.get(id=int(group_id))
        if request.user != group.leader:
            raise Exception('no authority to invite')
        if group.locked:
            raise Exception('group already locked')
        self.check_input(['username'])
        user = User.objects.get(username=request.data.get('username'))
        message = Invitation(group=group, invitee=user)
        message.save()


class MatchQuitView(View):
    @require_logged_in
    def post(self, request, contest_id: str, group_id: str)->Any:
        group = Group.objects.get(id=int(group_id))
        if group.locked:
            raise Exception('group already locked')
        if request.user == group.leader:
            group.members.remove(request.user)
            if len(group.members.all()) == 0:
                # delete foreign key first
                for stage in group.stage_list.all():
                    stage.delete()
                group.delete()
            else:
                member = group.members.first()
                group.members.remove(member)
                group.leader = member
                group.save()
        elif request.user in group.members:
            group.members.remove(request.user)
            group.save()
        else:
            raise Exception('not a group member')


class MatchLockView(View):
    @require_logged_in
    def post(self, request, contest_id: str, group_id: str)->Any:
        group = Group.objects.get(id=int(group_id))
        if group.locked:
            raise Exception('group already locked')
        if request.user != group.leader:
            raise Exception('no authority to lock group')
        group.locked = True
        group.save()


class MatchResponseView(View):
    @require_logged_in
    def post(self, request, contest_id: str, group_id: str)->Any:
        user = request.user
        self.check_input(['accept'])
        group = Group.objects.get(id=int(group_id))
        invitation = group.sent_invitations.get(invitee=user)
        accepted = request.data.get('accept')
        if accepted:
            group.members.add(user)
            group.save()
        invitation.status = InivationStatus.ACCEPTED if accepted else InivationStatus.REJECTED
        invitation.save()
        content = user.username + ('接受' if accepted else '拒绝') + '了你的邀请'
        message = Message(sender=User.objects.get(
            username='admin'), receiver=group.leader, content=content)
        message.save()


class MatchCancelView(View):
    @require_logged_in
    def post(self, request, contest_id: str, group_id: str)->Any:
        self.check_input(['username'])
        group = Group.objects.get(id=int(group_id))
        if group.leader != request.user:
            raise Exception('no authority to cancel invitation')
        user = User.objects.get(username=request.data.get('username'))
        invitation = group.sent_invitations.get(invitee=user)
        invitation.status = InivationStatus.CANCELLED
        invitation.save()


class MessageCollectionView(View):
    def get(self, request) -> Any:
        user = request.user
        self.check_input(['isRead'])
        is_read = int(request.data.get('isRead'))
        messages = user.received_messages.filter(is_read=is_read)
        invitations = user.received_invitations.filter(is_read=is_read)
        messageList = [{
            'id': m.id,
            'sender': m.sender.username,
            'content': m.content,
            'sendTime': m.send_time,
            'type': 'letter'
        } for m in messages]
        invitationList = [{
            'id': i.id,
            'sender': i.group.leader.username,
            'content': {
                'leaderName': i.group.leader.username,
                'groupName': i.group.name,
                'contestName': i.group.competition.name,
                'groupId': i.group.id,
                'contestId': i.group.competition.id,
                'status': i.status},
            'sendTime': i.send_time,
            'type': 'invitation',
        }for i in invitations]
        return messageList+invitationList

    def put(self, request) -> Any:
        self.check_input(['id', 'type'])
        category = request.data.get('type')
        if category == 'letter':
            message = Message.objects.get(id=request.data.get('id'))
            if request.user != message.receiver:
                raise Exception('no authority')
        elif category == 'invitation':
            message = Invitation.objects.get(id=request.data.get('id'))
            if request.user != message.invitee:
                raise Exception('no authority')
        if message.is_read:
            raise Exception('message already read')
        message.is_read = True
        message.save()

    def delete(self, request) -> Any:
        self.check_input(['id'])
        category = request.data.get('type')
        if category == 'letter':
            message = Message.objects.get(id=request.data.get('id'))
            if request.user != message.receiver:
                raise Exception('no authority')
        elif category == 'invitation':
            message = Invitation.objects.get(id=request.data.get('id'))
            if request.user != message.invitee:
                raise Exception('no authority')
        message.delete()

    def post(self, request) -> Any:
        self.check_input(['peer', 'content'])
        message = Message(
            sender=request.user,
            receiver=User.objects.get(username=request.data.get('peer')),
            content=request.data.get('content')
        )
        message.save()


class MessageUnreadView(View):
    def get(self, request) -> Any:
        lenM = len(request.user.received_messages.filter(is_read=False))
        lenI = len(request.user.received_invitations.filter(is_read=False))
        return {'count': lenM+lenI}
