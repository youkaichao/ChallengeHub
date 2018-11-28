from django.conf.urls import url
from match import views

urlpatterns = [
    url(r'users$',
        views.MatchUserView.as_view()),
    url(r'contests/(?P<contest_id>[0-9]+)/groups$',
        views.MatchGroupView.as_view()),
    url(r'contests/(?P<contest_id>[0-9]+)/groups/(?P<group_id>[0-9]+)/invitenew$',
        views.MatchInviteView.as_view()),
    url(r'contests/(?P<contest_id>[0-9]+)/groups/(?P<group_id>[0-9]+)/quit$',
        views.MatchQuitView.as_view()),
    url(r'contests/(?P<contest_id>[0-9]+)/groups/(?P<group_id>[0-9]+)/lock$',
        views.MatchLockView.as_view()),
]
