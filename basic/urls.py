from django.conf.urls import url
from basic import views

urlpatterns = [
    url(r'contest$', views.ContestView.as_view()),
]
