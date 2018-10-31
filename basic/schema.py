import graphene
from django.core.exceptions import ObjectDoesNotExist

from graphene_django.types import DjangoObjectType
from basic.models import Competition as CompetitionModel
from basic.models import Notice as NoticeModel
from basic.models import ContestantUser as ContestantUserModel
from basic.models import OrganizationUser as OrganizationUserModel
from basic.models import Group as GroupModel
from basic.models import ContestantGroupConnection
from basic.models import JudgeCompetitionConnection
from django.utils import timezone


class Competition(DjangoObjectType):
    class Meta:
        model = CompetitionModel

    judges = graphene.List(lambda: User)

    @staticmethod
    def resolve_judges(root, info):
        connections = JudgeCompetitionConnection.objects.filter(competition=root)
        return [connection.judge_user for connection in connections]


class CreateCompetition(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        subject = graphene.String()
        max_contestants = graphene.Int()
        enroll_start_time = graphene.DateTime()
        enroll_end_time = graphene.DateTime()
        detail = graphene.String()
        procedure = graphene.String()
        enroll_url = graphene.String()
        charge = graphene.Float()
        judging_standard = graphene.String()
        publisher_name = graphene.String()

    success = graphene.Boolean()
    competition_id = graphene.ID()

    @staticmethod
    def mutate(
            root, info,
            name, subject, max_contestants, enroll_start_time, enroll_end_time,
            detail, procedure, enroll_url, charge, judging_standard, publisher_name
    ):
        try:
            competition = CompetitionModel()
            competition.name = name
            competition.subject = subject
            competition.max_contestants = max_contestants
            competition.enroll_start_time = enroll_start_time
            competition.enroll_end_time = enroll_end_time
            competition.detail = detail
            competition.procedure = procedure
            competition.enroll_url = enroll_url
            competition.charge = charge
            competition.num_upvote = 0
            competition.num_downvote = 0
            competition.judging_standard = judging_standard
            competition.publisher = OrganizationUserModel.objects.get(name=publisher_name)
            competition.save()

            competition_id = competition.id
        except ObjectDoesNotExist:
            return CreateCompetition(success=False, competition_id=-1)
        else:
            return CreateCompetition(success=True, competition_id=competition_id)


class Notice(DjangoObjectType):
    class Meta:
        model = NoticeModel


class CreateNotice(graphene.Mutation):
    class Arguments:
        competition_id = graphene.ID()
        content = graphene.String()

    success = graphene.Boolean()

    @staticmethod
    def mutate(root, info, competition_id, content):
        notice = NoticeModel()
        notice.competition = CompetitionModel.objects.get(id=competition_id)
        notice.content = content
        notice.time_published = timezone.now()
        notice.save()
        return CreateNotice(success=True)


class User(DjangoObjectType):
    class Meta:
        model = ContestantUserModel
        exclude_fields = ('password_hash',)

    attended_competitions = graphene.List(Competition)

    @staticmethod
    def resolve_attended_competitions(root, info):
        group_connections = ContestantGroupConnection.objects.filter(contestant_user=root)
        return [group_connection.group.competition for group_connection in group_connections]


class CreateUser(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        password_hash = graphene.String()
        email_address = graphene.String()

    success = graphene.Boolean()

    @staticmethod
    def mutate(root, info, name, password_hash, email_address):
        if len(ContestantUserModel.objects.filter(name=name)) > 0:
            return CreateUser(success=False)
        user = ContestantUserModel()
        user.name = name
        user.password_hash = password_hash
        user.email_address = email_address
        user.introduction = ''
        user.source_school = ''
        user.save()
        return CreateUser(success=True)


class Organization(DjangoObjectType):
    class Meta:
        model = OrganizationUserModel
        exclude_fields = ('password_hash',)


class CreateOrganization(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        password_hash = graphene.String()
        email_address = graphene.String()
        introduction = graphene.String()

    success = graphene.Boolean()

    @staticmethod
    def mutate(root, info, name, password_hash, email_address):
        if len(OrganizationUserModel.objects.filter(name=name)) > 0:
            return CreateOrganization(success=False)

        organization = OrganizationUserModel()
        organization.name = name
        organization.password_hash = password_hash
        organization.email_address = email_address
        organization.introduction = ''
        organization.save()
        return CreateOrganization(success=True)


class Group(DjangoObjectType):
    class Meta:
        model = GroupModel

    members = graphene.List(User)

    @staticmethod
    def resolve_members(root, info):
        connections = ContestantGroupConnection.objects.filter(group=root)
        return [connection.contestant_user for connection in connections]


class CreateGroup(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        competition_id = graphene.ID()
        leader_name = graphene.String()

    success = graphene.Boolean()

    @staticmethod
    def mutate(root, info, name, competition_id, leader_name):
        if len(GroupModel.objects.filter(name=name)) > 0:
            return CreateGroup(success=False)
        group = GroupModel()
        group.name = name
        group.competition = CompetitionModel.objects.get(id=competition_id)
        group.leader_contestant = ContestantUserModel.objects.get(name=leader_name)
        group.commit_filepath = ""
        group.rank = ""
        group.save()
        return CreateGroup(success=True)


class JudgeInCompetition(graphene.ObjectType):
    user = graphene.Field(User)
    competition = graphene.Field(Competition)


class Query(graphene.ObjectType):
    all_competitions = graphene.List(Competition)
    competition_by_id = graphene.Field(Competition, competition_id=graphene.ID())
    all_organizations = graphene.List(Organization)
    judges_in_competition = graphene.List(JudgeInCompetition, competition_id=graphene.ID())
    all_users = graphene.List(User)

    @staticmethod
    def resolve_all_competitions(root, info):
        return CompetitionModel.objects.all()

    @staticmethod
    def resolve_competition_by_id(root, info, competition_id):
        return CompetitionModel.objects.filter(id=competition_id).first()

    @staticmethod
    def resolve_all_organizations(root, info):
        return OrganizationUserModel.objects.all()

    @staticmethod
    def resolve_judges_in_competition(root, info, competition_id):
        competition = CompetitionModel.objects.filter(id=competition_id).first()
        connections = JudgeCompetitionConnection.objects.filter(competition=competition)
        ret = []
        for connection in connections:
            judge_in_competition = JudgeInCompetition()
            judge_in_competition.user = connection.judge_user
            judge_in_competition.competition = competition
            ret.append(judge_in_competition)
        return ret

    @staticmethod
    def resolve_all_users(root, info):
        return ContestantUserModel.objects.all()


class Mutation(graphene.ObjectType):
    create_notice = CreateNotice.Field()
    create_competition = CreateCompetition.Field()
    create_user = CreateUser.Field()
    create_organization = CreateOrganization.Field()
    create_group = CreateGroup.Field()
