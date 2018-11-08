from django.conf.urls import url
from basic import views

urlpatterns = [
    url(r'contests$', views.ContestCollectionView.as_view()),
    url(r'contests/(?P<contest_id>[0-9]+)$',
        views.ContestDetailView.as_view()),
    url(r'contests/(?P<contest_id>[0-9]+)/enroll$',
        views.ContestEnrollView.as_view()),
    url(r'users$', views.UserCollectionView.as_view()),
    url(r'users/(?P<username>\w+)$', views.UserDetailView.as_view()),
    url(r'groups$', views.GroupCollectionView.as_view()),
    url(r'groups/(?P<group_id>[0-9]+)$', views.GroupDetailView.as_view())
]
