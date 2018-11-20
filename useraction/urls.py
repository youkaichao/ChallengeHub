from django.conf.urls import url
from useraction import views

urlpatterns = [
    url(r'login$', views.UserLoginView.as_view()),
    url(r'logout$', views.UserLogoutView.as_view()),
    url(r'register$', views.UserRegisterView.as_view()),
    url(r'info$', views.UserInfoView.as_view()),
    url(r'validate$', views.UserValidateView.as_view()),
]
