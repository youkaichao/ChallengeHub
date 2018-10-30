from django.contrib import admin
from basic.models import Competition
from basic.models import Notice
from basic.models import ContestantUser
from basic.models import OrganizationUser
from basic.models import Group
from basic.models import ContestantGroupConnection
from basic.models import JudgeCompetitionConnection

# Register your models here.
admin.site.register(Competition)
admin.site.register(Notice)
admin.site.register(ContestantUser)
admin.site.register(OrganizationUser)
admin.site.register(Group)
admin.site.register(ContestantGroupConnection)
admin.site.register(JudgeCompetitionConnection)
