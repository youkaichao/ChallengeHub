from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.core import serializers
from basic.models import Competition, Group
from useraction.models import User
from ChallengeHub.utils import *
from ChallengeHub.utils import BaseView as View
from ChallengeHub.settings import MONGO_CLIENT


class ContestCollectionView(View):
    def get(self, request):
        if 'sortBy' in request.data.keys():
            if request.data['sortBy'] == 'numVotes':
                competitions = Competition.objects.all().order_by('-upvote')
            else:
                competitions = Competition.objects.all()
        else:
            competitions = Competition.objects.all()
        return JsonResponse({'code': 0, "data": [competition.to_dict() for competition in competitions.all()]})

    def post(self, request):
        self.check_input([
            'name', 'subject', 'groupSize', 'enrollStart', 'enrollEnd',
            'detail', 'procedure', 'enrollUrl', 'charge', 'publisher', 'enrollForm', 'imgUrl',
        ])
        c = Competition(
            name=request.data.get('name'),
            subject=request.data.get('subject'),
            group_size=request.data.get('groupSize'),
            enroll_start=request.data.get('enrollStart'),
            enroll_end=request.data.get('enrollEnd'),
            detail=request.data.get('detail'),
            procedure=request.data.get('procedure'),
            enroll_url=request.data.get('enrollUrl'),
            charge=request.data.get('charge'),
            img_url=request.data.get('imgUrl'),
        )
        p = User.objects.get(username=request.data.get('publisher'))
        c.publisher = p
        c.save()
        collection = MONGO_CLIENT.competition.enrollForm
        collection.insert_one(
            {'id': c.id, 'enrollForm': request.data.get('enrollForm')})
        collection = MONGO_CLIENT.competition.stage
        collection.insert_one(
            {'id': c.id, 'stage': 0})
        if(not c.enroll_url):
            c.enroll_url = '/contest/enroll/{}'.format(c.id)
            c.save()
        return JsonResponse({'code': 0, 'data': c.to_dict()})


class ContestCollectionEnrolledView(View):
    def get(self, request):
        self.check_input(['username'])
        user = User.objects.get(username=request.data['username'])
        return JsonResponse({
            'code': 0,
            "data": [
                {
                    'group': group.to_dict(),
                    'contest': group.competition.to_dict()
                } for group in user.joint_groups.all()
            ]
        })


class ContestDetailView(View):
    def get(self, request, contest_id):
        c = Competition.objects.get(id=contest_id)
        info = c.to_dict(detail=True)
        collection = MONGO_CLIENT.competition.stage
        data = collection.find_one({'id': int(contest_id)})
        info['stage'] = data['stage']
        return JsonResponse({'code': 0, 'data': info})

    def post(self, request, contest_id):
        self.check_input(['stage'])
        collection = MONGO_CLIENT.competition.stage
        collection.find_one_and_update({'id': int(contest_id)}, {
                                       '$set': {'stage': request.data['stage']}})
        return JsonResponse({'code': 0, 'data': 'success'})


class GroupStageView(View):
    def post(self, request, contest_id):
        self.check_input(['group_ids', 'stage'])
        stage = request.data['stage']
        collection = MONGO_CLIENT.group.stage
        with MONGO_CLIENT.start_session() as session:
            with session.start_transaction():
                for id in request.data['group_ids']:
                    collection.find_one_and_update(
                        {'id': id}, {'$set': {'stage': stage}})
        return JsonResponse({'code': 0, 'data': 'success'})

    def get(self, request, contest_id):
        c = Competition.objects.get(id=contest_id)
        groups = c.enrolled_groups.all()
        groups_ids = [x.id for x in groups]
        collection = MONGO_CLIENT.group.stage
        data = [{'id': id, 'stage': collection.find_one(
            {'id': id})['stage']} for id in groups_ids]
        for (each, group) in zip(data, groups):
            each.update(group.to_dict())
        return JsonResponse({'code': 0, 'data': data})


class ContestEnrollView(View):
    def get(self, request, contest_id):
        collection = MONGO_CLIENT.competition.enrollForm
        data = collection.find_one({'id': int(contest_id)})
        return JsonResponse({'code': 0, 'data': {'enrollForm': data['enrollForm']}})

    def post(self, request, contest_id):
        self.check_input(['name', 'leaderName', 'members', 'form'])
        group = Group(
            name=request.data.get('name'),
            competition=Competition.objects.get(id=contest_id),
            leader=User.objects.get(
                username=request.data.get('leaderName'))
        )
        group.save()
        collection = MONGO_CLIENT.group.enrollForm
        collection.insert_one(
            {'id': group.id, 'enrollForm': request.data['form']})
        collection = MONGO_CLIENT.group.stage
        collection.insert_one(
            {'id': group.id, 'stage': 0})
        members = request.data['members']
        for member in members:
            group.members.add(User.objects.get(username=member))
        return JsonResponse({'code': 0, 'data': 'success'})


class UserCollectionView(View):
    def get(self, request):
        self.check_input(['type'])
        user_type = request.data['type']
        if user_type == 'organization':
            users = User.objects.filter(individual=False)
        elif user_type == 'contestant':
            # FIXME will select admins too
            users = User.objects.filter(individual=True)
        else:
            return JsonResponse(make_errors('invalid type'))
        return JsonResponse({'code': 0, 'data': [user.to_dict() for user in users]})

    def post(self, request):
        self.check_input([
            'username', 'firstName', 'lastName', 'email', 'introduction',
            'school', 'isIndividual'
        ])
        u = User(
            username=request.data.get['username'],
            first_name=request.data.get['firstName'],
            last_name=request.data.get['lastName'],
            email=request.data.get['email'],
            introduction=request.data.get['introduction'],
            school=request.data.get['school'],
            individual=request.data.get['isIndividual']
        )
        u.save()
        return JsonResponse({'code': 0, 'data': 'success'})


class UserDetailView(View):
    def get(self, request, username):
        u = User.objects.get(username=username)
        info = u.to_dict()
        return JsonResponse({'code': 0, 'data': info})


class UserCreatedView(View):
    def get(self, request):
        self.check_input(['username'])
        user = User.objects.get(username=request.data['username'])
        competitions = user.published_competitions.all()
        return JsonResponse({'code': 0, "data": [
            competition.to_dict() for competition in competitions]})


class UserJudgedView(View):
    def get(self, request):
        self.check_input(['username'])
        user = User.objects.get(username=request.data['username'])
        competitions = user.judged_competitions.all()
        return JsonResponse({'code': 0, "data": [
            competition.to_dict() for competition in competitions]})


class GroupCollectionView(View):
    def post(self, request):
        self.check_input([
            'name', 'competitionId', 'leaderName', 'membersName'
        ])
        g = Group(
            name=request.data['name'],
            competition=Competition.objects.get(
                id=request.data['competitionId']),
            leader=User.objects.get(username=request.data['leaderName'])
        )
        g.save()
        for member_name in request.data['membersName']:
            g.members.add(User.objects.get(username=member_name))
        g.save()
        return JsonResponse({'code': 0, 'data': 'success'})


class GroupDetailView(View):
    def get(self, request, group_id):
        g = Group.objects.get(id=group_id)
        info = g.to_dict()
        collection = MONGO_CLIENT.group.stage
        stage = collection.find_one({'id': int(group_id)})['stage']
        info['stage'] = stage
        return JsonResponse({'code': 0, 'data': info})
