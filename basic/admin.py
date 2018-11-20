from django.contrib import admin
from basic.models import Competition, CStage, Notice, Group, GStage, ReviewMeta

# Register your models here.
admin.site.register(Competition)
admin.site.register(CStage)
admin.site.register(Notice)
admin.site.register(Group)
admin.site.register(GStage)
admin.site.register(ReviewMeta)
