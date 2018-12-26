from django.shortcuts import render
from ChallengeHub.utils import BaseView as View, require_logged_in
from useraction.models import User
from match.models import Message, Invitation, InvitationStatus, ReviewerInvitation, MessageType, SystemMessage
from basic.models import Competition, Group
from ChallengeHub.settings import MONGO_CLIENT
from django.db.models import Q
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
            'members': [member.username for member in group.members.all()],
            'invitees': [i.invitee.username for i in
                         Invitation.objects.filter(group=group, status=InvitationStatus.DEFAULT)],
            'locked': group.locked,
        } for group in groups]


class MatchInviteView(View):
    @require_logged_in
    def post(self, request, contest_id: str, group_id: str) -> Any:
        group = Group.objects.get(id=int(group_id))
        if request.user != group.leader:
            raise Exception('没有权限邀请队员!')
        if group.locked:
            raise Exception('队伍已经锁定！')
        messages = Invitation.objects.filter(group=group, status=InvitationStatus.DEFAULT)
        num_members = len(group.members.all())
        contest = Competition.objects.get(id=int(contest_id))
        if num_members + len(messages) >= contest.group_size:
            raise Exception(
                f"当前队伍已经拥有 {num_members} 名成员，正在邀请 {len(messages)} 名成员, 然而比赛要求每个队伍的人数最多为 {contest.group_size} 。你不能再邀请队员了！")
        self.check_input(['username'])
        user = User.objects.get(username=request.data.get('username'))
        if user == group.leader:
            raise Exception("你不能邀请你自己！")
        message = Invitation.objects.filter(group=group, invitee=user, status=InvitationStatus.DEFAULT)
        if message:
            raise Exception(f'{user.username} 已经被邀请了！')
        elif user in group.members.all():
            raise Exception(f'{user.username} 已经是队员了！')
        else:
            message = Invitation(group=group, invitee=user)
            message.save()


class MatchQuitView(View):
    @require_logged_in
    def post(self, request, contest_id: str, group_id: str) -> Any:
        group = Group.objects.get(id=int(group_id))
        if group.locked:
            raise Exception('队伍已经锁定了！')
        if request.user == group.leader:
            group.members.remove(request.user)
            collection = MONGO_CLIENT.db.groupEnrollForm
            collection.delete_one({'user_id': request.user.id, 'contest_id': int(contest_id)})
            if len(group.members.all()) == 0:
                # delete foreign key first
                for stage in group.stage_list.all():
                    stage.delete()
                group.delete()
            else:
                member = group.members.first()
                group.leader = member
                group.save()
                for each in group.members.all():
                    message = SystemMessage(receiver=each, content=f'{request.user.username} 退出了队伍 {group.name}。 {group.leader.username} 现在是新的队长了！')
                    message.save()
        elif group.members.filter(id=request.user.id):
            group.members.remove(request.user)
            group.save()
            message = SystemMessage(receiver=group.leader, content=f'{request.user.username} 退出了队伍 {group.name}.')
            message.save()
        else:
            raise Exception('不是队伍的成员！')


class MatchLockView(View):
    @require_logged_in
    def post(self, request, contest_id: str, group_id: str) -> Any:
        group = Group.objects.get(id=int(group_id))
        if group.locked:
            raise Exception('队伍已经锁定了！')
        if request.user != group.leader:
            raise Exception('没有权限锁定队伍！')
        group.locked = True
        group.save()
        for each in group.members.all():
            message = SystemMessage(receiver=each, content=f'队伍 {group.name} 已经锁定了，你无法退出队伍了。')
            message.save()


class MatchResponseView(View):
    @require_logged_in
    def post(self, request, contest_id: str, group_id: str) -> Any:
        user = request.user
        self.check_input(['accept', 'form'])
        group = Group.objects.get(id=int(group_id))
        invitation = group.sent_invitations.get(invitee=user, status=InvitationStatus.DEFAULT)
        accepted = request.data.get('accept')
        if accepted:
            if user.joint_groups.filter(competition_id=group.competition.id):
                raise Exception('你已经参加了这场比赛了！')
            group.members.add(user)
            collection = MONGO_CLIENT.db.groupEnrollForm
            collection.insert_one(
                {'user_id': int(user.id), 'contest_id': int(contest_id), 'enrollForm': request.data['form']})
            group.save()
        invitation.status = InvitationStatus.ACCEPTED if accepted else InvitationStatus.REJECTED
        invitation.save()
        content = user.username + ('接受' if accepted else '拒绝') + '了你的邀请'
        message = SystemMessage(receiver=group.leader, content=content)
        message.save()


class ReviewersResponseView(View):
    @require_logged_in
    def post(self, request, contest_id: str) -> Any:
        user = request.user
        self.check_input(['accept', 'form'])
        c = Competition.objects.get(id=int(contest_id))
        invitation = c.sent_invitations.get(invitee=user, status=InvitationStatus.DEFAULT)
        accepted = request.data.get('accept')
        if accepted:
            c.judges.add(user)
            collection = MONGO_CLIENT.db.groupEnrollForm
            collection.insert_one(
                {'user_id': int(user.id), 'contest_id': int(contest_id), 'enrollForm': request.data['form']})
            c.save()
        invitation.status = InvitationStatus.ACCEPTED if accepted else InvitationStatus.REJECTED
        invitation.save()
        content = user.username + ('接受' if accepted else '拒绝') + '了你的邀请'
        message = SystemMessage(receiver=c.publisher, content=content)
        message.save()


class MatchCancelView(View):
    @require_logged_in
    def post(self, request, contest_id: str, group_id: str) -> Any:
        self.check_input(['username'])
        group = Group.objects.get(id=int(group_id))
        if group.leader != request.user:
            raise Exception('没有权限取消邀请！')
        user = User.objects.get(username=request.data.get('username'))
        invitation = group.sent_invitations.get(invitee=user, status=InvitationStatus.DEFAULT)
        invitation.status = InvitationStatus.CANCELLED
        invitation.save()


class ReviewersCancelView(View):
    @require_logged_in
    def post(self, request, contest_id: str) -> Any:
        self.check_input(['username'])
        c = Competition.objects.get(id=int(contest_id))
        if c.publisher != request.user:
            raise Exception('没有权限取消邀请！')
        user = User.objects.get(username=request.data.get('username'))
        invitation = c.sent_invitations.get(invitee=user, status=InvitationStatus.DEFAULT)
        invitation.status = InvitationStatus.CANCELLED
        invitation.save()


class MessageCollectionView(View):
    @require_logged_in
    def get(self, request) -> Any:
        user = request.user
        self.check_input(['isRead'])
        is_read = int(request.data.get('isRead'))
        messages = user.received_messages.filter(is_read=is_read)
        invitations = user.received_invitations.filter(is_read=is_read)
        reviewer_invitations = user.received_reviewer_invitations.filter(is_read=is_read)
        system_messages = user.received_system_messages.filter(is_read=is_read)
        messageList = [{
            'id': m.id,
            'sender': m.sender.username,
            'content': m.content,
            'sendTime': m.send_time,
            'type': MessageType.letter
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
            'type': MessageType.invitation,
        } for i in invitations]
        reviewer_invitations_list = [{
            'id': i.id,
            'sender': i.competition.publisher.username,
            'content': {
                'contestName': i.competition.name,
                'contestId': i.competition.id,
                'status': i.status},
            'sendTime': i.send_time,
            'type': MessageType.reviewer_invitation,
        } for i in reviewer_invitations]
        system_messages_list = [{
            'id': i.id,
            'content': i.content,
            'sendTime': i.send_time,
            'type': MessageType.system,
        } for i in system_messages]
        return messageList + invitationList + reviewer_invitations_list + system_messages_list

    @require_logged_in
    def put(self, request) -> Any:
        self.check_input(['id', 'type'])
        category = request.data.get('type')
        if category == MessageType.letter:
            message = Message.objects.get(id=request.data.get('id'))
            if request.user != message.receiver:
                raise Exception('没有权限！')
        elif category == MessageType.system:
            message = SystemMessage.objects.get(id=request.data.get('id'))
            if request.user != message.receiver:
                raise Exception('没有权限！')
        elif category == MessageType.invitation:
            message = Invitation.objects.get(id=request.data.get('id'))
            if request.user != message.invitee:
                raise Exception('没有权限！')
        elif category == MessageType.reviewer_invitation:
            message = ReviewerInvitation.objects.get(id=request.data.get('id'))
            if request.user != message.invitee:
                raise Exception('没有权限！')
        if message.is_read:
            raise Exception('消息已经是已读状态！')
        message.is_read = True
        message.save()

    @require_logged_in
    def post(self, request) -> Any:
        self.check_input(['peer', 'content'])
        message = Message(
            sender=request.user,
            receiver=User.objects.get(username=request.data.get('peer')),
            content=request.data.get('content')
        )
        message.save()
        return message.to_dict()


class MessageDeleteView(View):
    @require_logged_in
    def post(self, request) -> Any:
        self.check_input(['id', 'type'])
        category = request.data.get('type')
        if category == MessageType.letter:
            message = Message.objects.get(id=request.data.get('id'))
            if request.user != message.receiver:
                raise Exception('没有权限！')
        elif category == MessageType.system:
            message = SystemMessage.objects.get(id=request.data.get('id'))
            if request.user != message.receiver:
                raise Exception('没有权限！')
        elif category == MessageType.invitation:
            message = Invitation.objects.get(id=request.data.get('id'))
            if request.user != message.invitee:
                raise Exception('没有权限！')
        elif category == MessageType.reviewer_invitation:
            message = ReviewerInvitation.objects.get(id=request.data.get('id'))
            if request.user != message.invitee:
                raise Exception('没有权限！')
        message.delete()


class MessageUnreadView(View):
    @require_logged_in
    def get(self, request) -> Any:
        lenM = len(request.user.received_messages.filter(is_read=False))
        lenI = len(request.user.received_invitations.filter(is_read=False))
        lenR = len(request.user.received_reviewer_invitations.filter(is_read=False))
        lenS = len(request.user.received_system_messages.filter(is_read=False))
        return {'count': lenM + lenI + lenR + lenS}
