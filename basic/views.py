from django.db import transaction
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.utils import timezone
from basic.models import Competition, Group, CStage, GStage, ReviewMeta, Notice, Vote
from useraction.models import User
from match.models import Invitation
from typing import Dict, Any, Callable, List
from ChallengeHub.utils import BaseView as View, require_logged_in, make_errors, require_to_be_organization, \
    require_to_be_individual, require_to_be_publisher
from ChallengeHub.settings import MONGO_CLIENT, BASE_DIR
from match.models import Message, Invitation, InvitationStatus, ReviewerInvitation, SystemMessage
import os
import json
import libflow
import hashlib
import ChallengeHub.settings as settings
import urllib



class ContestCollectionView(View):
    def get(self, request) -> Any:
        competitions = Competition.objects.all()
        if 'search' in request.data:
            competitions = competitions.filter(
                name__icontains=request.data.get('search'))
        if 'sortBy' in request.data:
            if request.data['sortBy'] == 'numVotes':
                competitions = competitions.order_by('-upvote')
        return [competition.to_dict() for competition in competitions]

    @require_logged_in
    @require_to_be_organization
    def post(self, request) -> Any:
        self.check_input([
            'name', 'subject', 'groupSize', 'enrollStart', 'enrollEnd',
            'detail', 'procedure', 'enrollUrl', 'charge', 'enrollForm', 'imgUrl',
        ])
        contest_name = request.data.get('name')

        c = Competition(
            name=contest_name,
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
        collection = MONGO_CLIENT.db.competitionEnrollForm
        collection.insert_one(
            {'id': c.id, 'enrollForm': request.data.get('enrollForm')})
        return c.to_dict()


class ContestDetailView(View):
    def get(self, request, contest_id: str) -> Any:
        c = Competition.objects.get(id=int(contest_id))
        info = c.to_dict(detail=True)
        info['userRelated'] = {}
        if request.user.is_authenticated():
            vote = request.user.user_votes.filter(competition=c).first()
            info['userRelated']['upvoteStatus'] = vote.status if vote else 0
        else:
            info['userRelated']['upvoteStatus'] = 0
        return info

    @require_logged_in
    @require_to_be_organization
    @require_to_be_publisher
    def post(self, request, contest_id: str) -> Any:
        self.check_input(['stage'])
        competition = Competition.objects.get(id=int(contest_id))
        stage = int(request.data.get('stage'))

        if stage!= -1 and stage < competition.current_stage:
            raise Exception('Cannot proceed to previous stage')

        if stage > 0 and stage % 2 == 0:  # when enter judge stage, update all qualified group to that stage
            qualified_groups = Group.objects.filter(
                current_stage=competition.current_stage, competition=competition)
            qualified_groups.update(current_stage=stage)

        competition.current_stage = stage
        competition.save()
        return


class TaskStatView(View):
    @require_logged_in
    @require_to_be_organization
    @require_to_be_publisher
    def get(self, request, contest_id: str) -> Any:
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
        return {
            "totalTasks": total_tasks,
            "reviewedTasks": reviewed_tasks,
            "qualifiedGroups": len(qualified_groups),
            "submittedGroups": submitted_groups,
            "isAssigned": cstage.is_assigned
        }


class ContestReviewTaskView(View):
    @require_logged_in
    @require_to_be_organization
    @require_to_be_publisher
    def get(self, request, contest_id: str) -> Any:
        self.check_input(['stage'])
        stage = int(request.data['stage'])
        c = Competition.objects.get(id=int(contest_id))
        data = []
        for judge in c.judges.all():
            assigned = 0
            completed = 0
            for task in judge.review_list.all():
                gstage = task.stage
                if gstage.stage == stage - 1 and gstage.group.competition.id == int(contest_id):
                    assigned += 1
                    if task.reviewed:
                        completed += 1
            data.append({
                "username": judge.username,
                "email": judge.email,
                "assigned": assigned,
                "completed": completed
            })
        return data


class ContestAutoAssignView(View):
    @require_logged_in
    @require_to_be_organization
    @require_to_be_publisher
    def post(self, request, contest_id: str) -> Any:
        self.check_input(['stage', 'serious', 'maxconn', 'judges'])
        c = Competition.objects.get(id=int(contest_id))
        stage = int(request.data['stage'])
        maxconn = request.data['maxconn']
        serious = request.data['serious']
        avoidField = request.data.get('avoidField', '')
        judge_workloads = request.data['judges']
        judge_workloads = {x['username']: x['assign'] for x in judge_workloads}

        enroll_forms = MONGO_CLIENT.db.groupEnrollForm
        answer_map = {}
        answer_count = 0

        def get_id(ans):
            nonlocal answer_count, answer_map
            if ans not in answer_map:
                answer_map[ans] = answer_count
                answer_count += 1
            return answer_map[ans]

        def get_label(user):
            form = json.loads(enroll_forms.find_one({'user_id': user.id, 'contest_id': c.id})['enrollForm'])
            return get_id(form[avoidField])

        cstage = c.stage_list.get(stage=stage if stage % 2 == 1 else stage - 1)
        if cstage.is_assigned:
            raise Exception("already auto-assigned!")

        qualified_groups = c.enrolled_groups.filter(current_stage=stage)
        submitted_gstages = []
        group_token = {}
        for group in qualified_groups:
            gstage = group.stage_list.get(
                stage=stage if stage % 2 == 1 else stage - 1)
            if gstage.has_commit:
                submitted_gstages.append(gstage)
                if avoidField:
                    group_token[gstage.id] = get_label(group.leader)

        judges = list(c.judges.all())

        judge_count = {x.username: 0 for x in judges}
        group_count = {x.id: 0 for x in submitted_gstages}

        judge_token = {}
        if avoidField:
            for judge in judges:
                label = get_label(judge)
                judge_token[judge.username] = label

        libflow.set_max_conn(maxconn)
        libflow.set_use_token(not not avoidField)
        libflow.set_team_size(len(submitted_gstages))
        libflow.set_judge_size(len(judges))
        if avoidField:
            libflow.set_team_tokens([group_token[x.id] for x in submitted_gstages])
            libflow.set_judge_tokens([judge_token[x.username] for x in judges])
        judge_bottlenecks = []
        for judge in judges:
            work = judge_workloads.get(judge.username, 0)
            judge_bottlenecks.append(work)
        libflow.set_judge_bottlenecks(judge_bottlenecks)
        result = libflow.network_flow()
        for i in range(len(result)):
            assigns = result[i]
            for g_idx in assigns:
                judge_count[judges[i].username] += 1
                group_count[submitted_gstages[g_idx].id] += 1
                if serious:
                    review_meta = ReviewMeta(reviewer=judges[i], stage=submitted_gstages[g_idx])
                    review_meta.save()

        if serious:
            cstage.is_assigned = True
            cstage.save()
        groupNotFull = len(
            [key for key, value in group_count.items() if value < maxconn])
        groupZero = len(
            [key for key, value in group_count.items() if value == 0])
        if serious:
            judge_map = {x.username: x for x in judges}
            for name in judge_map:
                user = judge_map[name]
                message = SystemMessage(receiver=user, content=f'You are assigned {judge_count[name]} tasks in competition {c.name}')
                message.save()
        return {
            "judges": [
                {"username": judge.username, "assign": judge_count[judge.username]} for judge in judges
            ],
            "groupNotFull": groupNotFull,
            "groupZero": groupZero
        }


class ContestReviewerView(View):
    @require_logged_in
    @require_to_be_organization
    @require_to_be_publisher
    def post(self, request, contest_id: str) -> Any:
        self.check_input(['username'])
        c = Competition.objects.get(id=int(contest_id))
        invitations = c.sent_invitations.all()
        judges = c.judges.all()
        if len(set(request.data['username'])) != len(request.data['username']):
            raise Exception("duplicate username!")
        with transaction.atomic():
            for username in request.data['username']:
                user = User.objects.get(username=username)
                if user in judges:
                    raise Exception(f"{user.username} is already a judge of this competition!")
                if invitations.filter(status=InvitationStatus.DEFAULT, invitee=user):
                    raise Exception(f"{user.username} is already invited!")
                invitation = ReviewerInvitation(competition=c, invitee=user)
                invitation.save()
        return

    @require_logged_in
    @require_to_be_organization
    @require_to_be_publisher
    def get(self, request, contest_id: str) -> Any:
        c = Competition.objects.get(id=int(contest_id))
        judges = c.judges.all()
        data = [judge.to_dict() for judge in judges]
        for x in data:
            x['accepted'] = 1
        if request.data.get('all'):
            invited = c.sent_invitations.all().filter(status=InvitationStatus.DEFAULT)
            for x in invited:
                tmp = x.invitee.to_dict()
                tmp['accepted'] = 0
                data.append(tmp)
        for x in data:
            d = MONGO_CLIENT.db.groupEnrollForm.find_one({'user_id': int(x['id']), 'contest_id': int(contest_id)})
            if d:
                x['enrollForm'] = d['enrollForm']
            else:
                # not accepted invitation yet
                x['enrollForm'] = '{}'
        return data


class ContestVoteView(View):
    def post(self, request, contest_id: str) -> Any:
        self.check_input(['upvote'])
        c = Competition.objects.get(id=int(contest_id))
        vote = Vote.vote(c, request.user, request.data['upvote'])
        return {
            'upvote': c.upvote,
            'downvote': c.downvote,
            'upvoteStatus': vote.status,
        }


class GroupStageView(View):
    @require_logged_in
    @require_to_be_organization
    @require_to_be_publisher
    def post(self, request, contest_id: str) -> Any:
        self.check_input(['group_ids', 'stage'])
        stage = int(request.data['stage'])
        c = Competition.objects.get(id=int(contest_id))
        cstage = c.stage_list.all().get(stage=stage)
        with transaction.atomic():
            for id in request.data['group_ids']:
                group = Group.objects.get(id=id)
                group.current_stage = stage
                group.save()
                if group.stage_list.filter(stage=stage):
                    raise Exception(
                        f"stage {stage} already exists for group {group.name}")
                message = SystemMessage(receiver=group.leader, content=f'Your group {group.name} evolved into a new stage ({cstage.name})!')
                message.save()
                gstage = GStage(stage=stage, group=group, score=0.0)
                gstage.save()
        return

    @require_logged_in
    @require_to_be_organization
    @require_to_be_publisher
    def get(self, request, contest_id: str) -> Any:
        c = Competition.objects.get(id=int(contest_id))
        groups = c.enrolled_groups.all()
        data = [group.to_dict() for group in groups]
        return data


class GroupDetailView(View):
    @require_logged_in
    @require_to_be_organization
    @require_to_be_publisher
    def get(self, request, contest_id: str) -> Any:
        data = {}
        competition = Competition.objects.get(id=int(contest_id))
        collection = MONGO_CLIENT.db.competitionEnrollForm
        data['enrollForm'] = collection.find_one({'id': int(contest_id)})['enrollForm']
        groups = competition.enrolled_groups.all()
        data['info'] = [{
            'groupName': group.name,
            'name': user.username,
            'form': MONGO_CLIENT.db.groupEnrollForm.find_one({'user_id': int(user.id), 'contest_id': int(contest_id)})[
                'enrollForm']
        } for group in groups for user in group.members.all()]
        return data


class ContestEnrollView(View):
    def get(self, request, contest_id: str) -> Any:
        collection = MONGO_CLIENT.db.competitionEnrollForm
        data = collection.find_one({'id': int(contest_id)})
        return {'enrollForm': data['enrollForm']}

    @require_logged_in
    @require_to_be_individual
    def post(self, request, contest_id: str) -> Any:
        self.check_input(['name', 'leaderName', 'members', 'form'])
        leader = User.objects.get(username=request.data.get('leaderName'))
        c = Competition.objects.get(id=int(contest_id))
        joint_groups = leader.joint_groups.all().filter(competition=c)
        if joint_groups:
            raise Exception(f"you are already in group {joint_groups.first().name}")
        group = Group(
            name=request.data.get('name'),
            competition=c,
            leader=leader
        )
        group.save()
        # save first to have an ``id``
        group.members.add(group.leader)
        group.save()
        stage = GStage(stage=1, score=0, group=group)
        stage.save()

        collection = MONGO_CLIENT.db.groupEnrollForm
        collection.insert_one(
            {'user_id': int(group.leader.id), 'contest_id': int(contest_id), 'enrollForm': request.data['form']})
        members = request.data['members']
        for member in members:
            if member == request.data.get('leaderName'):
                continue
            user = User.objects.get(username=member)
            message = Invitation(group=group, invitee=user)
            message.save()
        return {'id': group.id}


class ContestSubmissionView(View):
    @require_logged_in
    @require_to_be_individual
    def post(self, request, contest_id: str) -> Any:
        user = request.user
        group = user.joint_groups.get(competition__id=int(contest_id))
        submit = request.data.get('file')
        stage = group.current_stage
        if stage != group.competition.current_stage or stage % 2 != 1:
            raise Exception('no authority to submit now')
        _, extension = os.path.splitext(submit.name)

        commit_dir = os.path.join('contest',
                                  contest_id, str(stage))
        commit_path = os.path.join(commit_dir, f'{group.id}{extension}')
        abs_dir = os.path.join(BASE_DIR, 'submit', commit_dir)
        abs_path = os.path.join(BASE_DIR, 'submit', commit_path)
        if (not os.path.exists(abs_dir)):
            os.makedirs(abs_dir)
        with open(abs_path, 'wb+') as f:
            for chunk in submit.chunks():
                f.write(chunk)
        group_stage = group.stage_list.get(stage=stage)
        group_stage.commit_path = os.path.join('/submit', commit_path)
        group_stage.submission = request.data.get('submissionName')
        group_stage.has_commit = True
        group_stage.save()
        return

    @require_logged_in
    @require_to_be_individual
    def get(self, request, contest_id: str) -> Any:
        user = request.user
        group = user.joint_groups.get(competition__id=int(contest_id))
        stage = request.data.get('stage', group.current_stage)
        stage = int(stage)
        if stage < 1:
            raise Exception('invalid stage')
        if stage % 2 == 0:
            stage = stage - 1
        group_stage = group.stage_list.get(stage=stage)
        if not group_stage.has_commit:
            raise Exception('not committed yet')
        return {
            'score': group_stage.score,
            'reviews': [{'rating': x.score, 'msg': x.msg} for x in group_stage.review_meta_list.all()],
            'submissionName': group_stage.submission,
            'url': group_stage.commit_path
        }


def compute_average_score(stage: GStage):
    reviews = stage.review_meta_list.all()
    sum = 0.0
    for x in reviews:
        sum += x.score
    if not reviews.count():
        stage.score = stage.deltaScore
    else:
        stage.score = sum / reviews.count() + stage.deltaScore
    stage.save()


class DeltaScoreView(View):
    @require_logged_in
    @require_to_be_organization
    @require_to_be_publisher
    def post(self, request, contest_id, gstage_id):
        self.check_input(['deltaScore', 'deltaMsg'])
        c = Competition.objects.get(id=int(contest_id))
        stage = GStage.objects.get(id=gstage_id)
        stage.deltaScore = float(request.data.get('deltaScore'))
        stage.deltaMsg = request.data.get('deltaMsg')
        message = SystemMessage(receiver=stage.group.leader, content=f'Your group {stage.group.name} has gained {stage.deltaScore} because of {stage.deltaMsg} in  competition {c.name}')
        message.save()
        compute_average_score(stage)


class BestowRankView(View):
    @require_logged_in
    @require_to_be_organization
    @require_to_be_publisher
    def post(self, request, contest_id):
        self.check_input(['rankName', 'ids'])
        rank_name = request.data.get('rankName')
        ids = request.data.get('ids')
        groups = Group.objects.filter(id__in=ids)
        c = Competition.objects.get(id=int(contest_id))
        for group in groups:
            group.rank = rank_name
            group.save()
            message = SystemMessage(receiver=group.leader, content=f'Your group {group.name} is awarded {rank_name} in competition {c.name}')
            message.save()


class UserCollectionView(View):
    @require_logged_in
    def get(self, request) -> Any:
        users = User.objects.all()
        if 'prefix' in request.data:
            users = users.filter(
                username__startswith=request.data.get('prefix'))
        return [{'username': user.username} for user in users]


class UserCreatedView(View):
    @require_logged_in
    @require_to_be_organization
    def get(self, request) -> Any:
        user = request.user
        competitions = user.published_competitions.all()
        return [competition.to_dict() for competition in competitions]


class UserJudgedView(View):
    @require_logged_in
    @require_to_be_individual
    def get(self, request) -> Any:
        user = request.user
        competitions = []
        contest_id_set = set()
        for r in user.review_list.all():
            tmp = r.stage.group.competition
            if tmp.id not in contest_id_set:
                contest_id_set.add(tmp.id)
                competitions.append(tmp)
        for tmp in user.judged_competitions.all():
            if tmp.id not in contest_id_set:
                contest_id_set.add(tmp.id)
                competitions.append(tmp)
        data = []
        for competition in competitions:
            stage = competition.current_stage
            stage = stage if stage % 2 == 1 else stage - 1
            reviews = user.review_list.filter(
                stage__group__competition=competition, stage__stage=stage)
            data.append({
                'contest': competition.to_dict(),
                'task': {
                    'count': reviews.count(),
                    'done': reviews.filter(reviewed=True).count()
                }
            })
        return data


class UserEnrolledView(View):
    @require_logged_in
    @require_to_be_individual
    def get(self, request) -> Any:
        user = request.user
        return [{
            'group': group.to_dict(),
            'contest': group.competition.to_dict()
        } for group in user.joint_groups.all()]


class JudgeReviewView(View):
    @require_logged_in
    @require_to_be_individual
    def get(self, request, contest_id: str) -> Any:
        def get_extension(pathname: str) -> str:
            _, extension = os.path.splitext(pathname)
            while len(extension) >= 1 and extension[0] == '.':
                extension = extension[1:]
            return extension

        competition = Competition.objects.get(id=int(contest_id))
        stage = request.data.get('stage', competition.current_stage)
        stage = int(stage)
        if stage == -1 or stage == 0:
            # contest ended or not started yet
            data = {'contest': competition.to_dict(), 'task': {"count":0, "done":0}, 'submissions': []}
            data['contest']['standard'] = ""
            return data
        stage = stage if stage % 2 == 1 else stage - 1
        data = {}
        data['contest'] = competition.to_dict()
        data['contest']['standard'] = competition.stage_list.get(
            stage=stage).criterion
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
            'msg': review.msg,
            'groupName': review.stage.group.name,
            'extension': get_extension(review.stage.commit_path)} for review in reviews]
        return data

    @require_logged_in
    @require_to_be_individual
    def post(self, request, contest_id: str) -> Any:
        self.check_input(['reviews'])
        reviews = request.data.get('reviews')
        for r in reviews:
            meta = ReviewMeta.objects.get(id=r['id'])
            meta.reviewed = meta.reviewed or r['reviewed']
            meta.score = r['rating']  # todo range test: what if score < 0 or score > 100?
            meta.msg = r.get('msg', '')
            meta.save()
            reviews = meta.stage.review_meta_list.all()
            sum = 0.0
            for x in reviews:
                sum += x.score
            meta.stage.score = sum / reviews.count() + meta.stage.deltaScore
            meta.stage.save()
        return


class CriterionView(View):
    @require_logged_in
    def get(self, request, contest_id: str) -> Any:
        self.check_input(['stage'])
        contest_id = int(contest_id)
        stage = int(request.data['stage'])
        if stage % 2 == 0:
            stage -= 1
        contest = Competition.objects.get(id=contest_id)
        cstage = CStage.objects.get(stage=stage, competition=contest)
        return {'criterion': cstage.criterion}

    @require_logged_in
    @require_to_be_organization
    @require_to_be_publisher
    def post(self, request, contest_id: str) -> Any:
        self.check_input([
            'stage', 'criterion'
        ])
        contest_id = int(contest_id)
        contest = Competition.objects.get(id=contest_id)
        stage = int(request.data['stage'])
        if stage % 2 == 0:
            stage -= 1
        criterion = request.data['criterion']
        cstage = CStage.objects.get(stage=stage, competition=contest)
        cstage.criterion = criterion
        cstage.save()
        return


class SubmissionAllView(View):
    @require_logged_in
    @require_to_be_organization
    @require_to_be_publisher
    def get(self, request, contest_id: str) -> Any:
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
                        'score': review.score,
                        'msg': review.msg,
                    })
                obj['judges'] = judges
                obj['deltaScore'] = submission.deltaScore
                obj['deltaMsg'] = submission.deltaMsg
                obj['id'] = submission.id
                res.append(obj)
        return res


class NoticeCollectionView(View):
    def get(self, request, contest_id: str) -> Any:
        competition = Competition.objects.get(id=int(contest_id))
        return {
            'notices': [notice.to_dict() for notice in Notice.objects.filter(competition=competition)],
            'contest': competition.to_dict(),
        }

    @require_logged_in
    @require_to_be_organization
    @require_to_be_publisher
    def post(self, request, contest_id: str) -> Any:
        competition = Competition.objects.get(id=int(contest_id))
        self.check_input(['title', 'content'])
        notice = Notice(
            competition=competition,
            title=request.data.get('title'),
            modified_time=timezone.now(),
            content=request.data.get('content'),
        )
        notice.save()
        for group in competition.enrolled_groups.all():
            for each in group.members.all():
                message = SystemMessage(receiver=each, content=f'{competition.publisher} published a notice ({notice.title}) in competition {competition.name}. Check it now!')
                message.save()
        return


class NoticeDetailView(View):
    def get(self, request, contest_id: str, notice_id: str) -> Any:
        notice = Notice.objects.get(id=int(notice_id))
        return notice.to_dict(detail=True)

    @require_logged_in
    @require_to_be_organization
    @require_to_be_publisher
    def delete(self, request, contest_id: str, notice_id: str) -> Any:
        competition = Competition.objects.get(id=int(contest_id))
        notice = Notice.objects.get(id=int(notice_id))
        notice.delete()
        return

    @require_logged_in
    @require_to_be_organization
    @require_to_be_publisher
    def put(self, request, contest_id: str, notice_id: str) -> Any:
        notice = Notice.objects.get(id=int(notice_id))
        self.check_input(['title', 'content'])
        notice.title = request.data.get('title')
        notice.content = request.data.get('content')
        notice.modified_time = timezone.now()
        notice.save()
        competition = Competition.objects.get(id=int(contest_id))
        for group in competition.enrolled_groups.all():
            for each in group.members.all():
                message = SystemMessage(receiver=each, content=f'{competition.publisher} modified the notice ({notice.title}) in competition {competition.name}. Check it now!')
                message.save()
        return


class UserProfileView(View):
    def get(self, request, username) -> Any:
        user = User.objects.get(username=username)
        return user.to_dict()

        
class ContestUploadView(View):
    @require_logged_in
    @require_to_be_organization
    def post(self, request) -> Any:
        submit = request.data.get('file')
        content = b''.join(submit.chunks())
        md5 = hashlib.md5(content).hexdigest()
        _, extension = os.path.splitext(submit.name)
        filename = md5 + extension
        dirname = os.path.join(settings.BASE_DIR, os.path.sep.join(['submit', 'img']))
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        with open(os.path.join(dirname, filename), 'wb') as f:
            f.write(content)
        return {"url":urllib.parse.urljoin(settings.SITE_URL, 'submit/img/' + filename)}