from django.conf.urls import url
from basic import views

urlpatterns = [
    url(r'contests$',
        views.ContestCollectionView.as_view()),
    url(r'contests/(?P<contest_id>[0-9]+)$',
        views.ContestDetailView.as_view()),
    url(r'contests/(?P<contest_id>[0-9]+)/enroll$',
        views.ContestEnrollView.as_view()),
    url(r'contests/(?P<contest_id>[0-9]+)/groups$',
        views.GroupStageView.as_view()),
    url(r'contests/(?P<contest_id>[0-9]+)/submission$',
        views.ContestSubmissionView.as_view()),
    url(r'users/enrolled$',
        views.UserEnrolledView.as_view()),
    url(r'users/judged$',
        views.UserJudgedView.as_view()),
    url(r'users/created$',
        views.UserCreatedView.as_view()),
    url(r'groups$',
        views.GroupCollectionView.as_view()),
    url(r'groups/(?P<group_id>[0-9]+)$',
        views.GroupDetailView.as_view()),
    url(r'judges/(?P<contest_id>[0-9]+)$',
        views.JudgeReviewView.as_view()),
]
