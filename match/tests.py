from django.test import TestCase
from ChallengeHub.utils import MyClient, delete_table
from basic.models import Competition, CStage, Notice, Group, GStage, ReviewMeta, Vote
from useraction.models import User
from match.models import Message, Invitation, InvitationStatus
from ChallengeHub.tests import teardown_all


def create_user(name):
    tmp = User.objects.filter(username=name)
    if not tmp:
        tmp = User.objects.create_user(username=name, password=name)
    else:
        tmp = tmp.first()
    tmp.save()
    globals()[name] = tmp
    return tmp


class MessageAPITest(TestCase):

    def setUp(self):
        # 创建这些用户并且释放到全局作用域中
        users = [create_user(x) for x in ['organizer', 'leader', 'student1', 'student2', 'reviewer1', 'admin']]
        organizer.individual = False
        organizer.save()

        m = Message(sender=leader, receiver=organizer, content='how is it going?')
        m.save()
        msg_id_1 = m.id
        m = Message(sender=leader, receiver=organizer, content='how is it going?')
        m.save()
        msg_id_2 = m.id
        m = Message(sender=student1, receiver=organizer, content='how is it going?')
        m.save()
        msg_id_3 = m.id
        m = Message(sender=student2, receiver=organizer, content='how is it going?')
        m.save()
        msg_id_4 = m.id

        self.ids = [msg_id_1, msg_id_2, msg_id_3, msg_id_4]

        # 变量 ``organizer``现在是包含用户名为``organizer``的浏览器
        for user in users:
            name = user.username
            tmp = MyClient()
            ans = tmp.login(username=name, password=name)
            globals()[name] = tmp

    def tearDown(self):
        teardown_all()


class GroupAPITest(TestCase):

    def setUp(self):
        # 创建这些用户并且释放到全局作用域中
        users = [create_user(x) for x in ['organizer', 'leader', 'student1', 'student2', 'reviewer1', 'admin']]
        organizer.individual = False
        organizer.save()

        # 创建比赛
        data = {
            "charge": 0,
            "detail": "nonsense",
            "enrollEnd": "2018-12-01T16:00:00.000Z",
            "enrollForm": '12',
            "enrollStart": "2018-11-29T16:00:00.000Z",
            "enrollUrl": "",
            "groupSize": 1,
            "imgUrl": "url????",
            "name": "pwf",
            "procedure": [{"name": "1st", "startTime": "2018-12-1", "endTime": "2018-12-3"},
                           {"name": "2nd", "startTime": "2018-12-4", "endTime": "2018-12-6"}],
            "publisher": "organizer",
            "subject": "pwf"
        }

        c = Competition(
            name=data.get('name'),
            subject=data.get('subject'),
            group_size=data.get('groupSize'),
            enroll_start=data.get('enrollStart'),
            enroll_end=data.get('enrollEnd'),
            detail=data.get('detail'),
            enroll_url=data.get('enrollUrl'),
            charge=data.get('charge'),
            img_url=data.get('imgUrl'),
            publisher=organizer
        )
        c.save()

        self.competition_id = c.id

        group = Group(
            name='name',
            competition=c,
            leader=leader)
        group.save()
        self.group_id = group.id

        invitation = Invitation(group=group, invitee=student1)
        invitation.save()

        # 变量 ``organizer``现在是包含用户名为``organizer``的浏览器
        for user in users:
            name = user.username
            tmp = MyClient()
            ans = tmp.login(username=name, password=name)
            globals()[name] = tmp

    def tearDown(self):
        teardown_all()


class GetAPITest(MessageAPITest):
    def test_get_apiv2_messages(self):
        data = organizer.get(f'/apiv2/messages', data={"isRead": 0})
        ids = [x['id'] for x in data['data']]
        self.assertEqual(set(ids), set(self.ids))

        data = organizer.get(f'/apiv2/messages', data={"isRead": 1})
        ids = [x['id'] for x in data['data']]
        self.assertEqual(set(ids), set())


class PutAPITest(MessageAPITest):
    def test_put_apiv2_messages(self):
        organizer.put(f'/apiv2/messages', data={"id": self.ids[0], 'type':'letter'})

        data = organizer.get(f'/apiv2/messages', data={"isRead": 0})
        ids = [x['id'] for x in data['data']]
        self.assertEqual(set(self.ids) - set(ids), {self.ids[0]})

        data = organizer.get(f'/apiv2/messages', data={"isRead": 1})
        ids = [x['id'] for x in data['data']]
        self.assertEqual(set(ids), {self.ids[0]})


class DeleteAPITest(MessageAPITest):
    def test_delete_apiv2_messages(self):
        organizer.post(f'/apiv2/messages/delete', data={"id": self.ids[1], 'type':'letter'})

        data = organizer.get(f'/apiv2/messages', data={"isRead": 0})
        ids = [x['id'] for x in data['data']]
        self.assertEqual(set(self.ids) - set(ids), {self.ids[1]})

        data = organizer.get(f'/apiv2/messages', data={"isRead": 1})
        ids = [x['id'] for x in data['data']]
        self.assertEqual(set(ids), set())


class CountAPITest(MessageAPITest):
    def test_count_apiv2_messages(self):
        data = organizer.get(f'/apiv2/messages/unread_count')
        self.assertEqual(data['data']['count'], len(self.ids))


class GetGroupsTest(GroupAPITest):
    def test_get_groups(self):
        data_1 = student1.get(f'/apiv2/contests/{self.competition_id}/groups')
        data_2 = student1.get(f'/apiv2/contests/{self.competition_id}/groups', {'username':'leader'})
        data_3 = student1.get(f'/apiv2/contests/{self.competition_id}/groups', {'teamId': self.group_id})
        self.assertEqual(data_1, data_2)
        self.assertEqual(data_2, data_3)
        self.assertEqual(data_1['data'][0]['teamId'], self.group_id)


class InviteGroupsTest(GroupAPITest):
    def test_invite_groups(self):
        data = student1.post(f'/apiv2/contests/{self.competition_id}/groups/{self.group_id}/invitenew')
        self.assertNotEqual(data['code'], 0)

        data = leader.post(f'/apiv2/contests/{self.competition_id}/groups/{self.group_id}/invitenew',
                           data={'username':'student2'})
        user = User.objects.get(username='student2')
        invitation = user.received_invitations.first()
        self.assertEqual(invitation.group.id, self.group_id)
        self.assertEqual(invitation.invitee, user)


class QuitGroupsTest(GroupAPITest):
    def test_quit_groups(self):
        data = leader.post(f'/apiv2/contests/{self.competition_id}/groups/{self.group_id}/quit')
        self.assertEqual(data['code'], 0)

        ans = Group.objects.filter(id=self.group_id)
        self.assertEqual(not not ans, False)


class LockGroupsTest(GroupAPITest):
    def test_lock_groups(self):
        data = leader.post(f'/apiv2/contests/{self.competition_id}/groups/{self.group_id}/lock')
        self.assertEqual(data['code'], 0)

        ans = Group.objects.get(id=self.group_id)
        self.assertEqual(ans.locked, True)


class ReplyGroupsTest(GroupAPITest):
    def test_reply_groups(self):
        data = student1.post(f'/apiv2/contests/{self.competition_id}/groups/{self.group_id}/invitation', data={'accept':True, "form":{}})
        self.assertEqual(data['code'], 0)

        ans = Group.objects.get(id=self.group_id)
        user = User.objects.get(username='student1')
        self.assertEqual(user in ans.members.all(), True)


class CancelGroupsTest(GroupAPITest):
    def test_cancel_groups(self):
        data = leader.post(f'/apiv2/contests/{self.competition_id}/groups/{self.group_id}/cancel', data={'username':'student1'})
        self.assertEqual(data['code'], 0)

        user = User.objects.get(username='student1')
        invitation = user.received_invitations.first()
        self.assertEqual(invitation.status, InvitationStatus.CANCELLED)