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
    procedure = models.TextField(default='')
    url = models.URLField(default='')
    charge = models.IntegerField(default=0)
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
    publisher = models.ForeignKey(User, on_delete=models.PROTECT)


class Notice(models.Model):
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    postedtime = models.DateTimeField(default=timezone.now)
    content = models.TextField(blank=False)


class Group(models.Model):
    name = models.CharField(max_length=32, blank=False)
    competition = models.ForeignKey(Competition, on_delete=models.PROTECT)
    leader = models.ForeignKey(User, on_delete=models.PROTECT)
    commitpath = models.FilePathField(blank=True)
    rank = models.TextField()


class UserGroupConnection(models.Model):
    group = models.ForeignKey(Group, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)


class JudgeCompetitionConnection(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    competition = models.ForeignKey(
        Competition, on_delete=models.DO_NOTHING)
