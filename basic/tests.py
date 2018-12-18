from django.core.files.base import ContentFile
from django.test import TestCase

from ChallengeHub.tests import teardown_all
from ChallengeHub.utils import MyClient
from basic.models import Competition, Group
from basic.views import ContestSubmissionView
from useraction.models import User


class BasicTest(TestCase):
    def setUp(self):
        self.publishers = {}
        self.judges = {}
        self.individuals = {}
        self.anonymous_client = MyClient()

    def add_user(self, username, type):
        if type not in ['publisher', 'individual', 'judge']:
            raise Exception('invalid user type')
        is_individual = type != 'publisher'
        user = User.objects.filter(username=username, individual=is_individual)
        if not user:
            user = User.objects.create_user(username=username, password=username, individual=is_individual)
            user.save()
        else:
            user = user.first()
        client = MyClient()
        res = client.login(username=username, password=username)
        self.assertTrue(res)
        obj = {
            'user': user,
            'client': client
        }

        if type == 'publisher':
            self.publishers[username] = obj
        elif type == 'judge':
            self.judges[username] = obj
        else:
            self.individuals[username] = obj

    def publish_contest(self, publisher_name, contest_name, stage_names, ignore_error=False):
        publisher_obj = self.publishers.get(publisher_name)
        contest_obj = {
            'name': contest_name,
            'subject': 'dummy',
            'groupSize': 3,
            'enrollStart': '2018-11-29T16:00:00.000Z',
            'enrollEnd': '2018-11-29T16:00:00.000Z',
            'detail': 'small detail',
            'procedure': [{
                'name': stage_name,
                'startTime': '2018-11-29T16:00:00.000Z',
                'endTime': '2018-11-29T16:00:00.000Z'
            } for stage_name in stage_names],
            'enrollUrl': '',
            'enrollForm': '[]',
            'charge': 0,
            'imgUrl': ''
        }
        resp = publisher_obj['client'].post('/api/contests', contest_obj)
        if not ignore_error:
            self.assertEqual(resp['code'], 0)
        return resp

    def proceed_publish_contest(self):
        admin = User(username='admin', individual=False, is_superuser=True)
        admin.set_password('admin')
        admin.save()
        self.add_user('a', 'publisher')
        self.add_user('b', 'publisher')
        self.add_user('c', 'individual')
        resp = self.anonymous_client.get('/api/contests')
        self.assertEqual(resp['code'], 0)
        self.assertEqual(len(resp['data']), 0)
        self.publish_contest('a', 'a_c', ['a', 'b'])
        self.publish_contest('b', 'b_c1', ['a', 'b', 'c'])
        self.publish_contest('b', 'b_c2', ['a'])

    def proceed_contest(self, publisher_name, contest_name, ignore_error=False):
        contest = Competition.objects.get(name=contest_name)
        client = self.publishers[publisher_name]['client']
        resp = client.post(f'/api/contests/{contest.id}', {
            'stage': contest.current_stage + 1
        })
        if not ignore_error:
            self.assertEqual(resp['code'], 0)
        return resp

    def tearDown(self):
        teardown_all()


class ContestCollectionTest(BasicTest):
    def setUp(self):
        super().setUp()
        self.proceed_publish_contest()

    def testAnonymousUserCanSee(self):
        resp = self.anonymous_client.get('/api/contests')
        self.assertEqual(resp['code'], 0)
        self.assertEqual(len(resp['data']), 3)

    def testAnonymousUserCanSearch(self):
        resp = self.anonymous_client.get('/api/contests', {'search': 'B_c'})
        self.assertEqual(resp['code'], 0)
        self.assertEqual(len(resp['data']), 2)

    def testCannotProceedToPreviousStage(self):
        contest = Competition.objects.get(name='a_c')
        client = self.publishers['a']['client']
        resp = client.post(f'/api/contests/{contest.id}', {
            'stage': contest.current_stage - 1
        })
        self.assertEqual(resp['error'], 'Cannot proceed to previous stage')


class VoteAndDetailTest(BasicTest):
    def setUp(self):
        super().setUp()
        self.proceed_publish_contest()
        self.a_c = Competition.objects.get(name='a_c')

    def testAnonymousCanSeeDetail(self):
        resp = self.anonymous_client.get(f'/api/contests/{self.a_c.id}')
        self.assertEqual(resp['data']['detail'], self.a_c.detail)

    def testOtherPublisherCannotChangeStage(self):
        resp = self.proceed_contest('b', 'a_c', ignore_error=True)
        self.assertEqual(resp['error'], 'no authority to change stage')

    def testCanVoteButOnlyOnce(self):
        client = self.individuals['c']['client']
        resp = client.post(f'/api/contests/{self.a_c.id}/vote', {
            'upvote': 1
        })
        obj_1 = resp['data']
        resp = client.post(f'/api/contests/{self.a_c.id}/vote', {
            'upvote': -1
        })
        obj_3 = resp['data']
        self.assertEqual(obj_1['upvote'] - 1, obj_3['upvote'])
        self.assertEqual(obj_1['downvote'] + 1, obj_3['downvote'])
        resp = client.post(f'/api/contests/{self.a_c.id}/vote', {
            'upvote': 0
        })

        obj_4 = resp['data']
        self.assertEqual(obj_3['upvote'], obj_4['upvote'])
        self.assertEqual(obj_3['downvote'], obj_4['downvote'])

    def testDetailSortByNumVote(self):
        client = self.individuals['c']['client']
        b_c1 = Competition.objects.get(name='b_c1')
        client.post(f'/api/contests/{b_c1.id}/vote', {
            'upvote': 1
        })
        resp = client.get('/api/contests', {
            'sortBy': 'numVotes'
        })
        self.assertEqual(resp['data'][0]['id'], b_c1.id)


class SubmissionTimeTest(BasicTest):
    def proceed_to_submit_time(self):
        self.proceed_publish_contest()
        self.proceed_contest('a', 'a_c')
        self.proceed_contest('b', 'b_c1')
        self.add_user('d', 'individual')
        self.add_user('e', 'individual')
        self.add_user('f', 'individual')
        self.add_user('g', 'judge')
        self.add_user('h', 'judge')
        a_c = Competition.objects.get(name='a_c')

        resp = self.individuals['c']['client'].post(f'/api/contests/{a_c.id}/enroll', {
            'name': 'c_t',
            'leaderName': 'c',
            'members': [],
            'form': '{}'
        })
        self.assertEqual(resp['code'], 0)
        c_id = resp['data']['id']
        resp = self.individuals['c']['client'].post(f'/apiv2/contests/{a_c.id}/groups/{c_id}/invitenew',
                                                    {'username': 'd'})
        self.assertEqual(resp['code'], 0)
        resp = self.individuals['d']['client'].post(f'/apiv2/contests/{a_c.id}/groups/{c_id}/invitation',
                                                    data={'accept': True, "form":{}})
        self.assertEqual(resp['code'], 0)

        resp = self.individuals['e']['client'].post(f'/api/contests/{a_c.id}/enroll', {
            'name': 'e_t',
            'leaderName': 'e',
            'members': [],
            'form': '{}'
        })
        self.assertEqual(resp['code'], 0)
        e_id = resp['data']['id']
        resp = self.individuals['e']['client'].post(f'/apiv2/contests/{a_c.id}/groups/{e_id}/invitenew',
                                                    {'username': 'f'})
        self.assertEqual(resp['code'], 0)
        resp = self.individuals['f']['client'].post(f'/apiv2/contests/{a_c.id}/groups/{e_id}/invitation',
                                                    data={'accept': True, "form":{}})
        self.assertEqual(resp['code'], 0)

    def setUp(self):
        super().setUp()
        self.proceed_to_submit_time()


class EnrollTest(SubmissionTimeTest):
    def testOneCanNotEnrollTwice(self):
        a_c = Competition.objects.get(name='a_c')
        resp = self.individuals['d']['client'].post(f'/api/contests/{a_c.id}/enroll', {
            'name': 'd_t',
            'leaderName': 'd',
            'members': [],
            'form': '{}'
        })
        self.assertTrue(resp['error'].startswith('you are already in group '))

    def testUserCreated(self):
        resp = self.publishers['b']['client'].get('/api/users/created')
        self.assertEqual(len(resp['data']), 2)

    def testUserCollection(self):
        resp = self.publishers['a']['client'].get('/api/users', {
            'prefix': 'd'
        })
        # note: /api/users also needs login
        self.assertEqual(len(resp['data']), 1)

    def testJointGroup(self):
        resp = self.individuals['d']['client'].get('/api/users/enrolled')
        self.assertEqual(len(resp['data']), 1)
        self.assertEqual(resp['data'][0]['group']['name'], 'c_t')

    def testCanSeeAllGroups(self):
        a_c = Competition.objects.get(name='a_c')
        resp = self.publishers['a']['client'].get(
            f'/api/contests/{a_c.id}/groups')
        self.assertEqual(len(resp['data']), 2)
        for group in resp['data']:
            self.assertEqual(group['stage'], 1)
        data = self.publishers['a']['client'].get(
            f'/api/contests/{a_c.id}/groups_detail')
        self.assertEqual(len(data['data']['info']), 2)
        data = self.anonymous_client.get(f'/api/contests/{a_c.id}/enroll')
        self.assertEqual(data['data']['enrollForm'], '[]')


class MockFile:
    def __init__(self, name, chunks):
        self.data = chunks
        self.name = name

    def chunks(self):
        return self.data


class MockRequest:
    def __init__(self, user, data):
        self.user = user
        self.data = data


class SubmittedTimeTest(SubmissionTimeTest):
    def setUp(self):
        super().setUp()
        self.a_c = Competition.objects.get(name='a_c')
        self.submit_file('d', self.a_c.id, 'd_sub',
                         MockFile('1234', [b'1', b'2', b'3']))
        self.submit_file('e', self.a_c.id, 'e_sub',
                         MockFile('123', [b'1', b'2']))

    def submit_file(self, username, contest_id, submission_name, file):
        ContestSubmissionView().post(MockRequest(user=User.objects.get(username=username),
                                                 data={
                                                     'submissionName': submission_name,
                                                     'file': file
        }), contest_id=str(contest_id))

    def add_judge(self, publisher_username, judge_username, contest_name):
        contest = Competition.objects.get(name=contest_name)
        resp = self.publishers[publisher_username]['client'].post(f'/api/contests/{contest.id}/reviewer', data={
            'username': [judge_username]
        })
        resp = self.judges[judge_username]['client'].post(f'/apiv2/contests/{contest.id}/reviewers/response', data={
            'accept': True, "form":{}
        })
        self.assertEqual(resp['code'], 0)


class SubmitListTest(SubmittedTimeTest):
    def testSubmissionList(self):
        resp = self.publishers['a']['client'].get(f'/api/contests/{self.a_c.id}/submission_all', {
            'stage': 1
        })
        self.assertEqual(len(resp['data']), 2)


class ReviewTimeTest(SubmittedTimeTest):
    def setUp(self):
        super().setUp()
        self.proceed_contest('a', 'a_c')
        self.add_judge('a', 'g', 'a_c')
        self.add_judge('a', 'h', 'a_c')
        a_c = Competition.objects.get(name='a_c')
        resp = self.publishers['a']['client'].post(f'/api/contests/{a_c.id}/auto_assign', data={
            'stage': a_c.current_stage,
            'maxconn': 2,
            'serious': True,
            'judges': [
                {
                    'username': 'g',
                    'assign': 2
                },
                {
                    'username': 'h',
                    'assign': 2
                }
            ]
        })
        self.assertEqual(resp['data']['groupNotFull'], 0)
        self.assertEqual(resp['data']['groupZero'], 0)


class ReviewerListTest(ReviewTimeTest):

    def testCannotAssignTwice(self):
        a_c = Competition.objects.get(name='a_c')
        resp = self.publishers['a']['client'].post(f'/api/contests/{a_c.id}/auto_assign', data={
            'stage': a_c.current_stage,
            'maxconn': 2,
            'serious': True,
            'judges': [
                {
                    'username': 'g',
                    'assign': 2
                },
                {
                    'username': 'h',
                    'assign': 2
                }
            ]
        })
        self.assertNotEqual(resp['code'], 0)
        self.assertEqual(resp['error'], 'already auto-assigned!')

    def testSeeReviewer(self):
        a_c = Competition.objects.get(name='a_c')
        client = self.publishers['a']['client']
        resp = client.get(f'/api/contests/{a_c.id}/reviewer')
        self.assertEqual(len(resp['data']), 2)
        judge_names = []
        for judge in resp['data']:
            judge_names.append(judge['username'])
        self.assertEqual(sorted(judge_names), sorted(['g', 'h']))

    def testCriterion(self):
        a_c = Competition.objects.get(name='a_c')
        criterion = 'abcde'
        resp = self.judges['g']['client'].get(f'/api/contests/{a_c.id}/criterion', {
            'stage': a_c.current_stage
        })
        self.assertEqual(resp['data']['criterion'], '')
        resp = self.publishers['a']['client'].post(f'/api/contests/{a_c.id}/criterion', data={
            'stage': a_c.current_stage,
            'criterion': criterion
        })
        self.assertEqual(resp['code'], 0)
        resp = self.judges['g']['client'].get(f'/api/contests/{a_c.id}/criterion', {
            'stage': a_c.current_stage
        })
        self.assertEqual(resp['data']['criterion'], criterion)


class JudgedTimeTest(ReviewTimeTest):
    def setUp(self):
        super().setUp()
        self.a_c = Competition.objects.get(name='a_c')
        self.c_t = Group.objects.get(name='c_t')
        self.e_t = Group.objects.get(name='e_t')
        resp = self.judges['g']['client'].post(f'/api/judges/{self.a_c.id}', data={'reviews': [{
            "id": self.c_t.stage_list.get(stage=self.c_t.current_stage - 1).review_meta_list.get(
                reviewer=self.judges['g']['user']).id,
            "reviewed": True,
            "rating": 80,
            "msg": "c"}]})
        self.assertEqual(resp['code'], 0)
        resp = self.judges['h']['client'].post(f'/api/judges/{self.a_c.id}', data={'reviews': [{
            "id": self.e_t.stage_list.get(stage=self.e_t.current_stage - 1).review_meta_list.get(
                reviewer=self.judges['h']['user']).id,
            "reviewed": True,
            "rating": 75,
            "msg": "e"}]})
        self.assertEqual(resp['code'], 0)


class JudgedTest(JudgedTimeTest):

    def testSubmission(self):
        resp = self.publishers['a']['client'].get(f'/api/contests/{self.a_c.id}/submission_all', {
            'stage': self.a_c.current_stage
        })
        done_c, done_e = False, False
        for submission in resp['data']:
            if submission['teamName'] == 'c_t':
                for judge in submission['judges']:
                    if judge['hasReviewed']:
                        self.assertEqual(judge['score'], 80)
                        done_c = True
            if submission['teamName'] == 'e_t':
                for judge in submission['judges']:
                    if judge['hasReviewed']:
                        self.assertEqual(judge['score'], 75)
                        done_e = True
        self.assertTrue(done_c and done_e)

    def testUserJudged(self):
        resp = self.judges['g']['client'].get('/api/users/judged')
        self.assertEqual(len(resp['data']), 1)
        self.assertEqual(resp['data'][0]['task']['done'], 1)
        self.assertEqual(resp['data'][0]['task']['count'], 2)

    def testUserSubmited(self):
        resp = self.individuals['d']['client'].get(
            f'/api/contests/{self.a_c.id}/submissions')
        self.assertEqual(resp['data']['score'], 40)

    def testReviewStatus(self):
        resp = self.publishers['a']['client'].get(f'/api/contests/{self.a_c.id}/reviewtask', {
            'stage': self.a_c.current_stage
        })
        self.assertEqual(len(resp['data']), 2)
        for judge in resp['data']:
            self.assertEqual(judge['assigned'], 2)
            self.assertEqual(judge['completed'], 1)

    def testTaskStat(self):
        resp = self.publishers['a']['client'].get(f'/api/contests/{self.a_c.id}/taskstat', {
            'stage': self.a_c.current_stage
        })
        self.assertEqual(resp['data']['totalTasks'], 4)
        self.assertEqual(resp['data']['reviewedTasks'], 2)
        self.assertEqual(resp['data']['qualifiedGroups'], 2)
        self.assertEqual(resp['data']['submittedGroups'], 2)
        self.assertEqual(resp['data']['isAssigned'], True)
