from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'add_competition$', views.add_competition),
    url(r'show_competition$', views.show_competition),
]
