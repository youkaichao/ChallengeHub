from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import logout, authenticate, login
from useraction.models import User
from ChallengeHub.utils import make_errors, require_logged_in
from ChallengeHub.utils import BaseView as View


class UserLoginView(View):
    def post(self, request) -> JsonResponse:
        self.check_input(['username', 'password'])
        user = authenticate(
            username=request.data.get('username'), password=request.data.get('password'))
        if(user and user.is_active):
            login(request, user)
            return JsonResponse({'code': 0, 'data': user.to_dict()})
        else:
            return JsonResponse(make_errors('wrong username or password'))


class UserInfoView(View):
    @require_logged_in
    def get(self, request) -> JsonResponse:
        return JsonResponse({'code': 0, 'data': request.user.to_dict()})

    @require_logged_in
    def post(self, request) -> JsonResponse:
        for name in ['email', 'introduction', 'school']:
            if request.data.get(name) != None:
                setattr(request.user, name, request.data.get(name))
        request.user.save()
        return JsonResponse({'code': 0, 'data': request.user.to_dict()})


class UserRegisterView(View):
    def post(self, request) -> JsonResponse:
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
    @require_logged_in
    def post(self, request) -> JsonResponse:
        logout(request)
        return JsonResponse({'code': 0, 'data': 'success'})
