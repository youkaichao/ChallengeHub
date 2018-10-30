import graphene

from graphene_django.types import DjangoObjectType
from basic.models import Competition as CompetitionModel
from basic.models import Notice as NoticeModel
from basic.models import ContestantUser as ContestantUserModel
from basic.models import OrganizationUser as OrganizationUserModel
from basic.models import Group as GroupModel
from basic.models import ContestantGroupConnection
from basic.models import JudgeCompetitionConnection


class Competition(DjangoObjectType):
    class Meta:
        model = CompetitionModel

    judges = graphene.List(lambda: User)

    @staticmethod
    def resolve_judges(root, info):
        connections = JudgeCompetitionConnection.objects.filter(competition=root)
        return [connection.judge_user for connection in connections]

class Notice(DjangoObjectType):
    class Meta:
        model = NoticeModel


class User(DjangoObjectType):
    class Meta:
        model = ContestantUserModel
        exclude_fields = ('password_hash',)

    attended_competitions = graphene.List(Competition)

    @staticmethod
    def resolve_attended_competitions(root, info):
        group_connections = ContestantGroupConnection.objects.filter(contestant_user=root)
        return [group_connection.group.competition for group_connection in group_connections]


class Organization(DjangoObjectType):
    class Meta:
        model = OrganizationUserModel
        exclude_fields = ('password_hash',)


class Group(DjangoObjectType):
    class Meta:
        model = GroupModel

    members = graphene.List(User)

    @staticmethod
    def resolve_members(root, info):
        connections = ContestantGroupConnection.objects.filter(group=root)
        return [connection.contestant_user for connection in connections]


class JudgeInCompetition(graphene.ObjectType):
    user = graphene.Field(User)
    competition = graphene.Field(Competition)


class Query(graphene.ObjectType):
    all_competitions = graphene.List(Competition)
    competition_by_id = graphene.Field(Competition, competition_id=graphene.ID())
    all_organizations = graphene.List(Organization)
    judges_in_competition = graphene.List(JudgeInCompetition, competition_id=graphene.ID())

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
