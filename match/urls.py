from django.conf.urls import url
from match import views

urlpatterns = [
    url(r'messages$',
        views.MessageCollectionView.as_view()),
    url(r'messages/delete$',
        views.MessageDeleteView.as_view()),
    url(r'messages/unread_count$',
        views.MessageUnreadView.as_view()),
    url(r'contests/(?P<contest_id>[0-9]+)/groups$',
        views.MatchGroupView.as_view()),
    url(r'contests/(?P<contest_id>[0-9]+)/groups/(?P<group_id>[0-9]+)/invitenew$',
        views.MatchInviteView.as_view()),
    url(r'contests/(?P<contest_id>[0-9]+)/groups/(?P<group_id>[0-9]+)/quit$',
        views.MatchQuitView.as_view()),
    url(r'contests/(?P<contest_id>[0-9]+)/groups/(?P<group_id>[0-9]+)/lock$',
        views.MatchLockView.as_view()),
    url(r'contests/(?P<contest_id>[0-9]+)/groups/(?P<group_id>[0-9]+)/invitation',
        views.MatchResponseView.as_view()),
    url(r'contests/(?P<contest_id>[0-9]+)/groups/(?P<group_id>[0-9]+)/cancel',
        views.MatchCancelView.as_view()),
]
