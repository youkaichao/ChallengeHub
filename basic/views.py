from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.views.generic import View
from django.core import serializers
from basic.models import Competition, Group
from useraction.models import User
from ChallengeHub.utils import *
from ChallengeHub.settings import MONGO_CLIENT


class ContestCollectionView(View):
    def get(self, request):
        try:
            if 'sortBy' in request.GET.keys():
                if request.GET['sortBy'] == 'numVotes':
                    competitions = Competition.objects.all().order_by('-upvote')
                else:
                    competitions = Competition.objects.all()
            else:
                competitions = Competition.objects.all()
            return JsonResponse({'code': 0, "data": [competition.to_dict() for competition in competitions.all()]})
        except Exception as e:
            return JsonResponse(make_errors(str(e)))

    def post(self, request):
        if not check_input(request.POST, [
            'name', 'subject', 'groupSize', 'enrollStart', 'enrollEnd',
            'detail', 'procedure', 'url', 'charge', 'publisher', 'enrollForm'
        ]):
            return JsonResponse(make_errors('invalid input'))
        c = Competition(
            name=request.POST.get('name'),
            subject=request.POST.get('subject'),
            group_size=request.POST.get('groupSize'),
            enroll_start=request.POST.get('enrollStart'),
            enroll_end=request.POST.get('enrollEnd'),
            detail=request.POST.get('detail'),
            procedure=request.POST.get('procedure'),
            url=request.POST.get('url'),
            charge=request.POST.get('charge'),
        )
        try:
            p = User.objects.get(username=request.POST.get('publisher'))
            c.publisher = p
            c.save()
            collection = MONGO_CLIENT.competition.enrollForm
            collection.insert_one(
                {'id': c.id, 'enrollForm': request.POST.get('enrollForm')})

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
            collection = MONGO_CLIENT.contest.enrollForm
            data = collection.find_one({'id': int(contest_id)})
            return JsonResponse({'code': 0, 'data': {'enrollForm': data.enrollForm}})
        except Exception as e:
            return JsonResponse(make_errors(str(e)))

    def post(self, request, contest_id):
        if not check_input(request.POST, ['name', 'leaderName', 'members[]', 'enrollForm']):
            return JsonResponse(make_errors('invalid input'))
        try:
            group = Group(
                name=request.POST.get('name'),
                competition=Competition.objects.get(id=contest_id),
                leader=User.objects.get(
                    username=request.POST.get('leaderName'))
            )
            group.save()
            collection = MONGO_CLIENT.group.enrollForm
            collection.insert_one(
                {'id': group.id, 'enrollForm': request.POST.get('enrollForm')})
            members = request.POST.getlist('members[]')
            for member in members:
                group.members.add(User.objects.get(username=member))
        except Exception as e:
            return JsonResponse(make_errors(str(e)))
        return JsonResponse({'code': 0, 'data': 'success'})


class UserCollectionView(View):
    def get(self, request):
        if check_input(request.GET, ['type']):
            user_type = request.GET['type']
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
        if not check_input(request.POST, [
            'username', 'firstName', 'lastName', 'email', 'introduction',
            'school', 'isIndividual'
        ]):
            return JsonResponse(make_errors('invalid input'))
        u = User(
            username=request.POST.get['username'],
            first_name=request.POST.get['firstName'],
            last_name=request.POST.get['lastName'],
            email=request.POST.get['email'],
            introduction=request.POST.get['introduction'],
            school=request.POST.get['school'],
            individual=request.POST.get['isIndividual']
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


class GroupCollectionView(View):
    def get(self, request):
        return JsonResponse(make_errors('method not allowed'))

    def post(self, request):
        if not check_input(request.POST, [
            'name', 'competitionId', 'leaderName', 'membersName'
        ]):
            return JsonResponse(make_errors('invalid input'))
        try:
            g = Group(
                name=request.POST['name'],
                competition=Competition.objects.get(
                    id=request.POST['competitionId']),
                leader=User.objects.get(username=request.POST['leaderName'])
            )
            g.save()
            for member_name in request.POST['membersName']:
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
