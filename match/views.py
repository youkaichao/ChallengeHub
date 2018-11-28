from django.shortcuts import render
from ChallengeHub.utils import BaseView as View, require_logged_in
from useraction.models import User
from match.models import Message, MessageType
from basic.models import Competition, Group
from typing import Any
import json
# Create your views here.


class MatchUserView(View):
    @require_logged_in
    def get(self, request) -> Any:
        users = User.objects.all()
        if 'prefix' in request.data:
            users = users.filter(
                username__startswith=request.data.get('prefix'))
        return [{'username': user.username} for user in users]


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
            'invitees': [m.receiver.username for m in Message.objects.filter(sender__username=group.leader.username, category=MessageType.INVITATION)],
            'locked': group.locked,
        } for group in groups]


class MatchInviteView(View):
    @require_logged_in
    def post(self, request, contest_id: str, group_id: str)->Any:
        group = Group.objects.get(id=int(group_id))
        if request.user != group.leader:
            raise Exception('no authority to invite')
        self.check_input(['username'])
        user = User.objects.get(username=request.data.get('username'))
        message = Message(category=MessageType.INVITATION, sender=request.user, receiver=user, content=json.dumps({
            'leaderName': request.user.username,
            'groupName': group.name,
            'contestName': group.competition.name
        }))
        message.save()


class MatchQuitView(View):
    @require_logged_in
    def post(self, request, contest_id: str, group_id: str)->Any:
        group = Group.objects.get(id=int(group_id))
        if group.locked:
            raise Exception('group already locked')
        if request.user == group.leader:
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
