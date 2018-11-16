from django.db import transaction
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.core import serializers
from basic.models import Competition, Group, CStage, GStage, ReviewMeta
from useraction.models import User
from ChallengeHub.utils import BaseView as View, require_logged_in, make_errors
from ChallengeHub.settings import MONGO_CLIENT, BASE_DIR
import os
import json


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
            enroll_url=request.data.get('enrollUrl'),
            charge=request.data.get('charge'),
            img_url=request.data.get('imgUrl'),
        )
        p = User.objects.get(username=request.data.get('publisher'))
        c.publisher = p
        c.save()
        procedure = request.data.get('procedure')
        for (i, prod) in enumerate(procedure):
            stage = CStage(name=prod["name"], start_time=prod["startTime"], end_time=prod["endTime"], stage=i+1, competition=c)
            stage.save()
        collection = MONGO_CLIENT.competition.enrollForm
        collection.insert_one(
            {'id': c.id, 'enrollForm': request.data.get('enrollForm')})
        if(not c.enroll_url):
            c.enroll_url = '/contest/enroll/{}'.format(c.id)
            c.save()
        return JsonResponse({'code': 0, 'data': c.to_dict()})


class ContestCollectionEnrolledView(View):
    @require_logged_in
    def get(self, request):
        user = request.user
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
        return JsonResponse({'code': 0, 'data': info})

    # def post(self, request, contest_id):
        # self.check_input(['stage'])
        # collection = MONGO_CLIENT.competition.stage
        # collection.find_one_and_update({'id': int(contest_id)}, {
                                       # '$set': {'stage': request.data['stage']}})
        # return JsonResponse({'code': 0, 'data': 'success'})


class GroupStageView(View):
    def post(self, request, contest_id):
        self.check_input(['group_ids', 'stage'])
        stage = request.data['stage']
        with transaction.atomic():
            for id in request.data['group_ids']:
                group = Group.objects.get(id=id)
                group.current_stage = stage
                group.save()
        return JsonResponse({'code': 0, 'data': 'success'})

    def get(self, request, contest_id):
        c = Competition.objects.get(id=contest_id)
        groups = c.enrolled_groups.all()
        data = [group.to_dict() for group in groups]
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
        g_stage = GStage(stage=1,score=0,group=group)
        g_stage.save()

        collection = MONGO_CLIENT.group.enrollForm
        collection.insert_one(
            {'id': group.id, 'enrollForm': request.data['form']})
        members = request.data['members']
        for member in members:
            group.members.add(User.objects.get(username=member))
        return JsonResponse({'code': 0, 'data': 'success'})


class ContestSubmitView(View):
    def post(self, request, contest_id):
        group_id = request.data.get('groupId')
        group = Group.objects.get(id=group_id)
        submit = request.data.get('file')
        stage = group.current_stage
        _, extension = os.path.splitext(submit.name)

        commit_dir = os.path.join('submit', 'contest',
                            contest_id, str(stage), f'{group_id}{extension}')
        commit_path = os.path.join(commit_dir, f'{group_id}{extension}')
        abs_dir = os.path.join(BASE_DIR, commit_dir)
        abs_path = os.path.join(BASE_DIR, commit_path)
        if(not os.path.exists(abs_dir)):
            os.makedirs(abs_dir)
        with open(abs_path, 'wb+') as f:
            for chunk in submit.chunks():
                f.write(chunk)
        group_stage = group.stage_list.get(stage=stage)
        group_stage.commit_path = commit_path
        group_stage.save()
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


class UserCreatedView(View):
    @require_logged_in
    def get(self, request):
        user = request.user
        competitions = user.published_competitions.all()
        return JsonResponse({'code': 0, "data": [
            competition.to_dict() for competition in competitions]})


class UserJudgedView(View):
    @require_logged_in
    def get(self, request):
        user = request.user
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
        return JsonResponse({'code': 0, 'data': g.to_dict()})
