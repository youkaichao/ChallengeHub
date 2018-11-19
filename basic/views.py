from django.db import transaction
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.utils import timezone
from basic.models import Competition, Group, CStage, GStage, ReviewMeta, Notice
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
        return JsonResponse({'code': 0, "data": [competition.to_dict() for competition in competitions]})

    def post(self, request):
        self.check_input([
            'name', 'subject', 'groupSize', 'enrollStart', 'enrollEnd',
            'detail', 'procedure', 'enrollUrl', 'charge', 'enrollForm', 'imgUrl',
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
            publisher=request.user
        )
        c.save()
        procedure = request.data.get('procedure')
        for (i, prod) in enumerate(procedure):
            stage = CStage(name=prod["name"], start_time=prod["startTime"],
                           end_time=prod["endTime"], stage=2 * i + 1, competition=c)
            stage.save()
        collection = MONGO_CLIENT.competition.enrollForm
        collection.insert_one(
            {'id': c.id, 'enrollForm': request.data.get('enrollForm')})
        if (not c.enroll_url):
            c.enroll_url = '/contest/enroll/{}'.format(c.id)
            c.save()
        return JsonResponse({'code': 0, 'data': c.to_dict()})


class ContestDetailView(View):
    def get(self, request, contest_id):
        c = Competition.objects.get(id=int(contest_id))
        info = c.to_dict(detail=True)
        return JsonResponse({'code': 0, 'data': info})

    def post(self, request, contest_id):
        self.check_input(['stage'])
        user = request.user
        competition = Competition.objects.get(id=int(contest_id))
        if (competition.publisher != user):
            raise Exception('no authority to change stage')
        stage = int(request.data.get('stage'))

        if stage > 0 and stage % 2 == 0:  # when enter judge stage, update all qualified group to that stage
            qualified_groups = Group.objects.filter(
                current_stage=competition.current_stage, competition=competition)
            qualified_groups.update(current_stage=stage)

        competition.current_stage = stage
        competition.save()
        return JsonResponse({'code': 0, 'data': 'success'})


class TaskStatView(View):
    def get(self, request, contest_id):
        self.check_input(['stage'])
        c = Competition.objects.get(id=int(contest_id))
        stage = int(request.data['stage'])
        cstage = c.stage_list.get(stage=stage if stage % 2 == 1 else stage - 1)
        qualified_groups = c.enrolled_groups.filter(current_stage=stage)
        submitted_groups = 0
        total_tasks = 0
        reviewed_tasks = 0
        for group in qualified_groups:
            gstage = group.stage_list.get(
                stage=stage if stage % 2 == 1 else stage - 1)
            if gstage.has_commit:
                submitted_groups += 1
            review_metas = gstage.review_meta_list.all()
            total_tasks += len(review_metas)
            for task in review_metas:
                if task.reviewed:
                    reviewed_tasks += 1
        return JsonResponse({
            'code': 0,
            'data': {
                "totalTasks": total_tasks,
                "reviewedTasks": reviewed_tasks,
                "qualifiedGroups": len(qualified_groups),
                "submittedGroups": submitted_groups,
                "isAssigned": cstage.is_assigned
            }})


class ContestReviewTaskView(View):
    def get(self, request, contest_id):
        self.check_input(['stage'])
        stage = int(request.data['stage'])
        c = Competition.objects.get(id=int(contest_id))
        data = []
        for judge in c.judges.all():
            assigned = 0
            completed = 0
            for task in judge.review_list.all():
                gstage = task.stage
                if gstage.stage == stage and gstage.group.competition.id == int(contest_id):
                    assigned += 1
                    if task.reviewed:
                        completed += 1
            data.append({
                "username": judge.username,
                "email": judge.email,
                "assigned": assigned,
                "completed": completed
            })
        return JsonResponse({'code': 0, 'data': data})


class ContestAutoAssignView(View):
    def post(self, request, contest_id):
        self.check_input(['stage', 'serious', 'maxconn', 'judges'])
        c = Competition.objects.get(id=int(contest_id))
        stage = int(request.data['stage'])
        maxconn = request.data['maxconn']
        serious = request.data['serious']
        cstage = c.stage_list.get(stage=stage if stage % 2 == 1 else stage - 1)
        if cstage.is_assigned:
            raise Exception("already auto-assigned!")
        qualified_groups = c.enrolled_groups.filter(current_stage=stage)
        submitted_gstages = []
        for group in qualified_groups:
            gstage = group.stage_list.get(
                stage=stage if stage % 2 == 1 else stage - 1)
            if gstage.has_commit:
                submitted_gstages.append(gstage)
        judges = list(c.judges.all())

        judge_count = {x.username: 0 for x in judges}
        group_count = {x.id: 0 for x in submitted_gstages}

        if cstage.is_assigned and serious:
            raise Exception("already assigned")

        # assign assignment
        index = 0
        for gstage in submitted_gstages:
            for i in range(maxconn):
                judge = judges[index % len(judges)]
                index += 1
                judge_count[judge.username] += 1
                group_count[gstage.id] += 1
                if serious:
                    review_meta = ReviewMeta(reviewer=judge, stage=gstage)
                    review_meta.save()
        if serious:
            cstage.is_assigned = True
            cstage.save()
        groupNotFull = len(
            [key for key, value in group_count.items() if value < maxconn])
        groupZero = len(
            [key for key, value in group_count.items() if value == 0])
        return JsonResponse({'code': 0, 'data': {
            "judges": [
                {"username": judge.username, "assign": judge_count[judge.username]} for judge in judges
            ],
            "groupNotFull": groupNotFull,
            "groupZero": groupZero
        }})


class ContestReviewerView(View):
    def post(self, request, contest_id):
        self.check_input(['username'])
        c = Competition.objects.get(id=int(contest_id))
        with transaction.atomic():
            for username in request.data['username']:
                user = User.objects.get(username=username)
                c.judges.add(user)
            c.save()
        return JsonResponse({'code': 0, 'data': 'success'})

    def get(self, request, contest_id):
        c = Competition.objects.get(id=int(contest_id))
        judges = c.judges.all()
        data = [judge.to_dict() for judge in judges]
        return JsonResponse({'code': 0, 'data': data})


class GroupStageView(View):
    def post(self, request, contest_id):
        self.check_input(['group_ids', 'stage'])
        stage = int(request.data['stage'])
        with transaction.atomic():
            for id in request.data['group_ids']:
                group = Group.objects.get(id=id)
                group.current_stage = stage
                group.save()
                if group.stage_list.filter(stage=stage):
                    raise Exception(
                        f"stage {stage} already exists for group {group.name}")
                gstage = GStage(stage=stage, group=group, score=0.0)
                gstage.save()
        return JsonResponse({'code': 0, 'data': 'success'})

    def get(self, request, contest_id):
        c = Competition.objects.get(id=int(contest_id))
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
            competition=Competition.objects.get(id=int(contest_id)),
            leader=User.objects.get(
                username=request.data.get('leaderName'))
        )
        group.save()
        stage = GStage(stage=1, score=0, group=group)
        stage.save()

        collection = MONGO_CLIENT.group.enrollForm
        collection.insert_one(
            {'id': group.id, 'enrollForm': request.data['form']})
        members = request.data['members']
        for member in members:
            group.members.add(User.objects.get(username=member))
        return JsonResponse({'code': 0, 'data': 'success'})


class ContestSubmissionView(View):
    def post(self, request, contest_id):
        user = request.user
        group = user.joint_groups.get(competition__id=int(contest_id))
        submit = request.data.get('file')
        stage = group.current_stage
        if (stage != group.competition.current_stage or stage % 2 != 1):
            raise Exception('no authority to submit now')
        _, extension = os.path.splitext(submit.name)

        commit_dir = os.path.join('contest',
                                  contest_id, str(stage), f'{group.id}{extension}')
        commit_path = os.path.join(commit_dir, f'{group.id}{extension}')
        abs_dir = os.path.join(BASE_DIR, 'submit', commit_dir)
        abs_path = os.path.join(BASE_DIR, 'submit', commit_path)
        if (not os.path.exists(abs_dir)):
            os.makedirs(abs_dir)
        with open(abs_path, 'wb+') as f:
            for chunk in submit.chunks():
                f.write(chunk)
        group_stage = group.stage_list.get(stage=stage)
        group_stage.commit_path = os.path.join('/static', commit_path)
        group_stage.submission = request.data.get('submissionName')
        group_stage.has_commit = True
        group_stage.save()
        return JsonResponse({'code': 0, 'data': 'success'})

    def get(self, request, contest_id):
        user = request.user
        group = user.joint_groups.get(competition__id=int(contest_id))
        stage = request.data.get('stage', group.current_stage)
        if stage < 1:
            raise Exception('invalid stage')
        if stage % 2 == 0:
            stage = stage - 1
        group_stage = group.stage_list.get(stage=stage)
        if not group_stage.has_commit:
            raise Exception('not committed yet')
        return JsonResponse({
            'code': 0,
            'data': {
                'submissionName': group_stage.submission,
                'url': group_stage.commit_path
            }})


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
        competitions = [
            r.stage.group.competition for r in user.review_list.all()]
        data = []
        for competition in competitions:
            reviews = user.review_list.filter(
                stage__group__competition=competition, stage__stage=competition.current_stage)
            data.append({
                'contest': competition.to_dict(),
                'task': {
                    'count': reviews.count(),
                    'done': len(reviews.filter(reviewed=True))
                }
            })
        return JsonResponse({
            'code': 0,
            "data": data,
        })


class UserEnrolledView(View):
    @require_logged_in
    def get(self, request):
        user = request.user
        return JsonResponse({
            'code': 0,
            'data': [
                {
                    'group': group.to_dict(),
                    'contest': group.competition.to_dict()
                } for group in user.joint_groups.all()
            ]
        })


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
        g = Group.objects.get(id=int(group_id))
        return JsonResponse({'code': 0, 'data': g.to_dict()})


class JudgeReviewView(View):
    def get(self, request, contest_id):
        def get_extension(pathname: str) -> str:
            _, extension = os.path.splitext(pathname)
            while len(extension) >= 1 and extension[0] == '.':
                extension = extension[1:]
            return extension

        competition = Competition.objects.get(id=int(contest_id))
        stage = request.data.get('stage', competition.current_stage)
        stage = stage if stage % 2 == 1 else stage - 1
        data = {}
        data['contest'] = competition.to_dict()
        reviews = request.user.review_list.filter(
            stage__group__competition=competition, stage__stage=stage)
        data['task'] = {
            'count': reviews.count(),
            'done': reviews.filter(reviewed=True).count()
        }
        data['submissions'] = [{
            'id': review.id,
            'submissionName': review.stage.submission,
            'reviewed': review.reviewed,
            'rating': review.score,
            'url': review.stage.commit_path,
            'extension': get_extension(review.stage.commit_path)} for review in reviews]
        return JsonResponse({'code': 0, 'data': data})

    def post(self, request, contest_id):
        self.check_input(['reviews'])
        competition = Competition.objects.get(id=int(contest_id))
        reviews = request.data.get('reviews')
        for r in reviews:
            meta = ReviewMeta.objects.get(id=r['id'])
            meta.reviewed = meta.reviewed or r['reviewed']
            meta.score = r['rating']
            meta.save()
            reviews = meta.stage.review_meta_list.all()
            sum = 0.0
            for x in reviews:
                sum += x.score
            meta.stage.score = sum / reviews.count()
            meta.stage.save()
        return JsonResponse({'code': 0, 'data': 'success'})


class CriterionView(View):
    def get(self, request, contest_id):
        self.check_input(['stage'])
        contest_id = int(contest_id)
        stage = int(request.data['stage'])
        if stage % 2 == 0:
            stage -= 1
        contest = Competition.objects.get(id=contest_id)
        cstage = CStage.objects.get(stage=stage, competition=contest)
        return JsonResponse({'code': 0, 'data': {
            'criterion': cstage.criterion
        }})

    def post(self, request, contest_id):
        self.check_input([
            'stage', 'criterion'
        ])
        contest_id = int(contest_id)
        stage = int(request.data['stage'])
        if stage % 2 == 0:
            stage -= 1
        criterion = request.data['criterion']
        contest = Competition.objects.get(id=contest_id)
        cstage = CStage.objects.get(stage=stage, competition=contest)
        cstage.criterion = criterion
        cstage.save()
        return JsonResponse({'code': 0, 'data': ''})


class SubmissionAllView(View):
    def get(self, request, contest_id):
        self.check_input(['stage'])
        contest_id = int(contest_id)
        stage = int(request.data['stage'])
        if stage % 2 == 0:
            stage -= 1
        contest = Competition.objects.get(id=contest_id)
        submissions = GStage.objects.filter(
            stage=stage, group__competition=contest)
        res = []
        for submission in submissions:
            if submission.has_commit:
                obj = {}
                obj['teamName'] = submission.group.name
                obj['name'] = submission.submission
                obj['downloadUrl'] = submission.commit_path
                obj['score'] = submission.score
                judges = []
                review_set = ReviewMeta.objects.filter(stage=submission)
                for review in review_set:
                    judges.append({
                        'username': review.reviewer.username,
                        'hasReviewed': review.reviewed,
                        'score': review.score
                    })
                obj['judges'] = judges
                res.append(obj)
        return JsonResponse({'code': 0, 'data': res})


class NoticeCollectionView(View):
    def get(self, request, contest_id):
        return JsonResponse({
            'code': 0,
            'data': [notice.to_dict() for notice in Notice.objects.filter(competition__id=int(contest_id))],
        })

    def post(self, request, contest_id):
        competition = Competition.objects.get(id=int(contest_id))
        if request.user != competition.publisher:
            raise Exception('no authority to publish notice')
        self.check_input(['title', 'content'])
        notice = Notice(
            competition=competition,
            title=request.data.get('title'),
            modified_time=timezone.now,
            content=request.data.get('content'),
        )
        return JsonResponse({'code': 0, 'data': 'success'})


class NoticeDetailView(View):
    def get(self, request, contest_id, notice_id):
        notice = Notice.objects.get(id=int(notice_id))
        return JsonResponse({
            'code': 0,
            'data': notice.to_dict(detail=True)
        })

    def delete(self, request, contest_id, notice_id):
        competition = Competition.objects.get(id=int(contest_id))
        if request.user != competition.publisher:
            raise Exception('no authority to delete notice')
        notice = Notice.objects.get(id=int(notice_id))
        notice.delete()
        return JsonResponse({'code': 0, 'data': 'success', })

    def put(self, request, contest_id, notice_id):
        competition = Competition.objects.get(id=int(contest_id))
        if request.user != competition.publisher:
            raise Exception('no authority to modify notice')
        notice = Notice.objects.get(id=int(notice_id))
        self.check_input(['title', 'content'])
        notice.title = request.data.get('title')
        notice.content = request.data.get('content')
        notice.modified_time = timezone.now
        notice.save()
        return JsonResponse({'code': 0, 'data': 'success'})
