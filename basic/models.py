import json
from django.db import models
import django.utils.timezone as timezone
from useraction.models import User


class Competition(models.Model):
    name = models.CharField(max_length=32, blank=False)
    subject = models.CharField(max_length=10, blank=False)
    group_size = models.IntegerField(default=1)
    enroll_start = models.DateTimeField(default=timezone.now)
    enroll_end = models.DateTimeField(default=timezone.now)
    detail = models.TextField(default='')
    img_url = models.URLField(default='')
    enroll_url = models.URLField(default='')
    charge = models.IntegerField(default=0)
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
    publisher = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='published_competitions')
    judges = models.ManyToManyField(User, related_name='judged_competitions')
    current_stage = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def to_dict(self, detail=False):
        data = {
            'id': self.id,
            'name': self.name,
            'subject': self.subject,
            'groupSize': self.group_size,
            'enrollStart': self.enroll_start,
            'enrollEnd': self.enroll_end,
            'imgUrl': self.img_url,
            'enrollUrl': self.enroll_url,
            'charge': self.charge,
            'upvote': self.upvote,
            'downvote': self.downvote,
            'publisher': self.publisher.username,
            'stage': self.current_stage,
            'procedure': [stage.to_dict() for stage in self.stage_list.all()]
        }
        if detail:
            data['detail'] = self.detail
        return data


"""
CStage: competition stage data
"""


class CStage(models.Model):
    name = models.CharField(max_length=32, blank=False)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
    criterion = models.TextField(default='')
    stage = models.IntegerField()
    competition = models.ForeignKey(
        Competition, related_name='stage_list', on_delete=models.PROTECT)
    is_assigned = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def to_dict(self, detail=False):
        data = {
            'name': self.name,
            'startTime': self.start_time.strftime('%Y-%m-%d'),
            'endTime': self.end_time.strftime('%Y-%m-%d'),
            'stage': self.stage,
            'isAssigned': self.is_assigned
        }
        if detail:
            data['criterion'] = self.criterion
        return data


class Notice(models.Model):
    competition = models.ForeignKey(
        Competition, on_delete=models.CASCADE, related_name='published_notices')
    title = models.CharField(default='', max_length=50)
    modified_time = models.DateTimeField(default=timezone.now)
    content = models.TextField(blank=False)

    def __str__(self):
        return f'{self.competition}: {self.content}'

    def to_dict(self, detail=False):
        data = {
            'id': self.id,
            'competitionId': self.competition.id,
            'competitionName': self.competition.name,
            'modifiedTime': self.modified_time.strftime('%Y-%m-%d'),
            'title': self.title,
        }
        if detail:
            data['content'] = self.content
        return data


class Group(models.Model):
    name = models.CharField(max_length=32, blank=False)
    competition = models.ForeignKey(
        Competition, on_delete=models.PROTECT, related_name='enrolled_groups')
    leader = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='lead_groups')
    members = models.ManyToManyField(
        User, related_name='joint_groups')
    rank = models.TextField()
    current_stage = models.IntegerField(default=1)

    def __str__(self):
        return self.name

    def to_dict(self, detail=False):
        return {
            'id': self.id,
            'name': self.name,
            'competitionId': self.competition.id,
            'competitionName': self.competition.name,
            'hasCommit': self.stage_list.get(stage=self.current_stage if self.current_stage % 2 == 1 else self.current_stage - 1).has_commit,
            'leaderName': self.leader.username,
            'membersName': [member.username for member in self.members.all()],
            'rank': self.rank,
            'stage': self.current_stage
        }


"""
GStage: group stage data
"""


class GStage(models.Model):
    stage = models.IntegerField()
    has_commit = models.BooleanField(default=False)
    commit_path = models.FilePathField(blank=True)
    submission = models.CharField(default='', max_length=50)
    score = models.FloatField(default=0.0)
    group = models.ForeignKey(
        Group, related_name='stage_list', on_delete=models.PROTECT)

    def to_dict(self, detail=False):
        data = {
            'stage': self.stage,
            'commitPath': self.commit_path,
            'score': self.score,
        }
        return data


"""
ReviewMeta: meta data for each reviewer with each group each stage
"""


class ReviewMeta(models.Model):
    reviewer = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='review_list')
    score = models.FloatField(default=0.0)
    reviewed = models.BooleanField(default=False)
    stage = models.ForeignKey(
        GStage, related_name='review_meta_list', on_delete=models.PROTECT)
    msg = models.CharField(max_length=256, blank=False)

    def to_dict(self, detail=False):
        data = {
            'reviewer': self.reviewer.username,
            'score': self.score,
            'msg': self.msg
        }
        return data


class Vote(models.Model):
    competition = models.ForeignKey(
        Competition, related_name='competition_votes', on_delete=models.PROTECT)
    user = models.ForeignKey(User, related_name='user_votes',
                             on_delete=models.PROTECT)
    status = models.IntegerField(default=0)

    @classmethod
    def vote(cls, competition: Competition, user: User, upvote: int):
        if not user.is_authenticated():
            raise Exception("not logged in")
        vote = Vote.objects.filter(competition=competition, user=user).first()
        if not vote or vote.status == 0:
            if not vote:
                vote = Vote(competition=competition, user=user, status=upvote)
            else:
                vote.status = upvote
            if upvote > 0:
                competition.upvote += 1
            elif upvote < 0:
                competition.downvote += 1
        else:
            if vote.status == upvote:
                vote.status = 0
                if upvote > 0:
                    competition.upvote -= 1
                elif upvote < 0:
                    competition.downvote -= 1
            else:
                vote.status = upvote
                if upvote > 0:
                    competition.upvote += 1
                    competition.downvote -= 1
                elif upvote < 0:
                    competition.upvote -= 1
                    competition.downvote += 1
        vote.save()
        competition.save()
        return vote
