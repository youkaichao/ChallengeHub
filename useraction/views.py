from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import logout, authenticate, login
from useraction.models import User
from ChallengeHub.utils import check_input, make_errors
from ChallengeHub.utils import BaseView as View


class UserLoginView(View):
    def get(self, request):
        return JsonResponse(make_errors('no such method'))

    def post(self, request):
        if(not check_input(request.data, ['username', 'password'])):
            return JsonResponse(make_errors('invalid input'))
        user = authenticate(
            username=request.data.get('username'), password=request.data.get('password'))
        if(user and user.is_active):
            login(request, user)
            return JsonResponse({'code': 0, 'data': {
                'username': user.username,
                'email': user.email,
                'introduction': user.introduction,
                'school': user.school,
                'individual': user.individual
            }})
        else:
            return JsonResponse(make_errors('wrong username or password'))


class UserRegisterView(View):
    def get(self, request):
        return JsonResponse(make_errors('no such method'))

    def post(self, request):
        available = check_input(
            request.data, ['username', 'password', 'email', 'individual'])
        if(not available):
            return JsonResponse(make_errors('Invalid input'))
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
        return JsonResponse({'code': 0, 'data': {
            'name': user.username,
            'email': user.email,
            'introduction': user.introduction,
            'school': user.school,
            'individual': user.individual
        }})


class UserLogoutView(View):
    def get(self, request):
        return JsonResponse(make_errors('no such method'))

    def post(self, request):
        logout(request)
        return JsonResponse({'code': 0, 'data': 'success'})
