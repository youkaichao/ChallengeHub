from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import logout, authenticate, login
from useraction.models import User
from ChallengeHub.utils import make_errors
from ChallengeHub.utils import BaseView as View


class UserLoginView(View):
    def post(self, request):
        self.check_input(['username', 'password'])
        user = authenticate(
            username=request.data.get('username'), password=request.data.get('password'))
        if(user and user.is_active):
            login(request, user)
            return JsonResponse({'code': 0, 'data': user.to_dict()})
        else:
            return JsonResponse(make_errors('wrong username or password'))


class UserInfoView(View):
    def get(self, request):
        self.check_input(['username'])
        user = User.objects.get(username=request.data.get('username'))
        if(not user or not user.is_active):
            return JsonResponse(make_errors('user not logged in'))
        return JsonResponse({'code': 0, 'data': user.to_dict()})


class UserRegisterView(View):
    def post(self, request):
        self.check_input(['username', 'password', 'email', 'individual'])
        user = User.objects.filter(username=request.data.get('username'))
        if(user):
            return JsonResponse(make_errors('username already exists'))
        user = User.objects.create_user(
            username=request.data.get('username'),
            password=request.data.get('password'),
            email=request.data.get('email'),
            individual=True if(request.data.get('individual')
                               == 'individual') else False
        )
        user.save()
        login(request, user)
        return JsonResponse({'code': 0, 'data': user.to_dict()})


class UserLogoutView(View):
    def post(self, request):
        logout(request)
        return JsonResponse({'code': 0, 'data': 'success'})
