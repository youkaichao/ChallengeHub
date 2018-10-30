from django.db import models
import django.utils.timezone as timezone
# Create your models here.


class OrganizationUser(models.Model):
    name = models.CharField(max_length=32, blank=False, primary_key=True)
    password_hash = models.CharField(max_length=512, blank=False)
    email_address = models.EmailField(blank=False)
    introduction = models.TextField()


class Competition(models.Model):
    # `id` will be added automatically
    name = models.CharField(max_length=32, blank=False)
    subject = models.CharField(max_length=10, blank=False)
    max_contestants = models.IntegerField(default=1)
    enroll_start_time = models.DateTimeField(default=timezone.now)
    enroll_end_time = models.DateTimeField(default=timezone.now)
    detail = models.TextField(default='')
    procedure = models.TextField(default='')
    enroll_url = models.URLField(default='')
    charge = models.IntegerField(default=0)
    num_upvote = models.IntegerField(default=0)
    num_downvote = models.IntegerField(default=0)
    judging_standard = models.TextField(default='')
    publisher = models.ForeignKey(OrganizationUser, on_delete=models.PROTECT)


class Notice(models.Model):
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    time_published = models.DateTimeField(default=timezone.now)
    content = models.TextField(blank=False)


class ContestantUser(models.Model):
    name = models.CharField(max_length=32, blank=False, primary_key=True)
    password_hash = models.CharField(max_length=512, blank=False)
    email_address = models.EmailField(blank=False)
    introduction = models.TextField()
    source_school = models.CharField(max_length=64)


class Group(models.Model):
    name = models.CharField(max_length=32, blank=False)
    competition = models.ForeignKey(Competition, on_delete=models.PROTECT)
    leader_contestant = models.ForeignKey(ContestantUser, on_delete=models.PROTECT)
    commit_filepath = models.FilePathField(blank=True)
    rank = models.TextField()  # json, dynamically parsed by frontend


class ContestantGroupConnection(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    contestant_user = models.ForeignKey(ContestantUser, on_delete=models.CASCADE)


class JudgeCompetitionConnection(models.Model):
    judge_user = models.ForeignKey(ContestantUser, on_delete=models.CASCADE)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    task = models.TextField()  # json, dynamically parsed by frontend


# TODO `GroupMatchingWilling`
# TODO `PrizeDelivery`
# TODO `Feedback`
