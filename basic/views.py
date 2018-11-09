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
        try:
            if 'sortBy' in request.data.keys():
                if request.data['sortBy'] == 'numVotes':
                    competitions = Competition.objects.all().order_by('-upvote')
                else:
                    competitions = Competition.objects.all()
            else:
                competitions = Competition.objects.all()
            return JsonResponse({'code': 0, "data": [competition.to_dict() for competition in competitions.all()]})
        except Exception as e:
            return JsonResponse(make_errors(str(e)))

    def post(self, request):
        if not check_input(request.data, [
            'name', 'subject', 'groupSize', 'enrollStart', 'enrollEnd',
            'detail', 'procedure', 'url', 'charge', 'publisher', 'enrollForm'
        ]):
            return JsonResponse(make_errors('invalid input'))
        c = Competition(
            name=request.data.get('name'),
            subject=request.data.get('subject'),
            group_size=request.data.get('groupSize'),
            enroll_start=request.data.get('enrollStart'),
            enroll_end=request.data.get('enrollEnd'),
            detail=request.data.get('detail'),
            procedure=request.data.get('procedure'),
            url=request.data.get('url'),
            charge=request.data.get('charge'),
        )
        try:
            p = User.objects.get(username=request.data.get('publisher'))
            c.publisher = p
            c.save()
            collection = MONGO_CLIENT.competition.enrollForm
            collection.insert_one(
                {'id': c.id, 'enrollForm': request.data.get('enrollForm')})

        except Exception as e:
            return JsonResponse(make_errors(str(e)))
        return JsonResponse({'code': 0, 'data': c.to_dict()})


class ContestDetailView(View):
    def get(self, request, contest_id):
        try:
            c = Competition.objects.get(id=contest_id)
            info = c.to_dict()
            return JsonResponse({'code': 0, 'data': info})
        except Exception as e:
            return JsonResponse(make_errors(str(e)))

    def post(self):
        return JsonResponse(make_errors('method not allowed'))


class ContestEnrollView(View):
    def get(self, request, contest_id):
        try:
            collection = MONGO_CLIENT.competition.enrollForm
            data = collection.find_one({'id': int(contest_id)})
            return JsonResponse({'code': 0, 'data': {'enrollForm': data['enrollForm']}})
        except Exception as e:
            return JsonResponse(make_errors(str(e)))

    def post(self, request, contest_id):
        if not check_input(request.data, ['name', 'leaderName', 'members', 'enrollForm']):
            return JsonResponse(make_errors('invalid input'))
        try:
            group = Group(
                name=request.data.get('name'),
                competition=Competition.objects.get(id=contest_id),
                leader=User.objects.get(
                    username=request.data.get('leaderName'))
            )
            group.save()
            collection = MONGO_CLIENT.group.enrollForm
            collection.insert_one(
                {'id': group.id, 'enrollForm': request.data.get('enrollForm')})
            members = request.data.get('members')
            for member in members:
                group.members.add(User.objects.get(username=member))
        except Exception as e:
            return JsonResponse(make_errors(str(e)))
        return JsonResponse({'code': 0, 'data': 'success'})


class UserCollectionView(View):
    def get(self, request):
        if check_input(request.data, ['type']):
            user_type = request.data['type']
            if user_type == 'organization':
                users = User.objects.filter(individual=False)
            elif user_type == 'contestant':
                # FIXME will select admins too
                users = User.objects.filter(individual=True)
            else:
                return JsonResponse(make_errors('invalid type'))
            return JsonResponse({'code': 0, 'data': [user.to_dict() for user in users]})
        else:
            return JsonResponse(make_errors('method not allowed'))

    def post(self, request):
        if not check_input(request.data, [
            'username', 'firstName', 'lastName', 'email', 'introduction',
            'school', 'isIndividual'
        ]):
            return JsonResponse(make_errors('invalid input'))
        u = User(
            username=request.data.get['username'],
            first_name=request.data.get['firstName'],
            last_name=request.data.get['lastName'],
            email=request.data.get['email'],
            introduction=request.data.get['introduction'],
            school=request.data.get['school'],
            individual=request.data.get['isIndividual']
        )
        try:
            u.save()
        except Exception as e:
            return JsonResponse(make_errors(str(e)))
        return JsonResponse({'code': 0, 'data': 'success'})


class UserDetailView(View):
    def get(self, request, username):
        try:
            u = User.objects.get(username=username)
            info = u.to_dict()
            return JsonResponse({'code': 0, 'data': info})
        except Exception as e:
            return JsonResponse(make_errors(str(e)))

    def post(self, request):
        return JsonResponse(make_errors('method not allowed'))


class UserCreatedView(View):
    def get(self, request):
        if(not check_input(request.data, ['username'])):
            return JsonResponse(make_errors('invalid input'))
        try:
            user = User.objects.get(username=request.data['username'])
            competitions = user.published_competitions.all()
            return JsonResponse({'code': 0, "data": [
                competition.to_dict() for competition in competitions]})
        except Exception as e:
            return JsonResponse(make_errors(str(e)))

    def post(self, request):
        return JsonResponse(make_errors('method not allowed'))


class UserEnrolledView(View):
    def get(self, request):
        if(not check_input(request.data, ['username'])):
            return JsonResponse(make_errors('invalid input'))
        try:
            user = User.objects.get(username=request.data['username'])
            groups = user.joint_groups.all()
            return JsonResponse({'code': 0, "data": [
                group.competition.to_dict() for group in groups]})
        except Exception as e:
            return JsonResponse(make_errors(str(e)))

    def post(self, request):
        return JsonResponse(make_errors('method not allowed'))


class UserJudgedView(View):
    def get(self, request):
        if(not check_input(request.data, ['username'])):
            return JsonResponse(make_errors('invalid input'))
        try:
            user = User.objects.get(username=request.data['username'])
            competitions = user.judged_competitions.all()
            return JsonResponse({'code': 0, "data": [
                competition.to_dict() for competition in competitions]})
        except Exception as e:
            return JsonResponse(make_errors(str(e)))

    def post(self, request):
        return JsonResponse(make_errors('method not allowed'))


class GroupCollectionView(View):
    def get(self, request):
        return JsonResponse(make_errors('method not allowed'))

    def post(self, request):
        if not check_input(request.data, [
            'name', 'competitionId', 'leaderName', 'membersName'
        ]):
            return JsonResponse(make_errors('invalid input'))
        try:
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
        except Exception as e:
            return JsonResponse(make_errors(str(e)))
        return JsonResponse({'code': 0, 'data': 'success'})


class GroupDetailView(View):
    def get(self, request, group_id):
        try:
            g = Group.objects.get(id=group_id)
            info = g.to_dict()
        except Exception as e:
            return JsonResponse(make_errors(str(e)))
        return JsonResponse({'code': 0, 'data': info})

    def post(self, request):
        return JsonResponse(make_errors('method not allowed'))
