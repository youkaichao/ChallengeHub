from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import logout, authenticate, login
from django.core.mail import send_mail
from useraction.models import User
from ChallengeHub.utils import make_errors, require_logged_in
from ChallengeHub.utils import BaseView as View
from typing import Dict, Any, Callable, List
from ChallengeHub.settings import EMAIL_FROM, SITE_URL, VALIDATE_SALT, USE_MAIL_VALIDATE
import base64
import hashlib


class UserLoginView(View):
    def post(self, request) -> Any:
        self.check_input(['username', 'password'])
        user = authenticate(
            username=request.data.get('username'), password=request.data.get('password'))
        if user and user.is_active:
            login(request, user)
            return user.to_dict()
        elif not user:
            raise Exception('wrong username or password')
        else:
            raise Exception('user will stay inactive until validated')


class UserInfoView(View):
    @require_logged_in
    def get(self, request) -> Any:
        return request.user.to_dict()

    @require_logged_in
    def post(self, request) -> Any:
        for name in ['email', 'introduction', 'school']:
            if request.data.get(name) != None:
                setattr(request.user, name, request.data.get(name))
        request.user.save()
        return request.user.to_dict()


class UserRegisterView(View):
    def post(self, request) -> Any:
        self.check_input(['username', 'password', 'email', 'individual'])
        user = User.objects.filter(username=request.data.get('username'))
        if user:
            raise Exception('username already exists')
        if User.objects.filter(email=request.data.get('email')):
            raise Exception('email is already registered')
        user = User.objects.create_user(
            username=request.data.get('username'),
            password=request.data.get('password'),
            email=request.data.get('email'),
            individual=True if (request.data.get('individual')
                                == 'individual') else False,
            is_active=not USE_MAIL_VALIDATE
        )
        m = hashlib.md5()
        m.update((user.email + VALIDATE_SALT).encode('utf-8'))
        encoded = base64.urlsafe_b64encode(
            f'{user.username}&{m.hexdigest()}'.encode('utf-8'))
        link = f'http://{SITE_URL}/#/validate/{encoded.decode()}'
        if USE_MAIL_VALIDATE:
            send_mail(
                subject='Validate your email account on ChanllengeHub',
                message=f'{user.username}, please validate your email account by visiting the link below\n{link}',
                from_email=EMAIL_FROM,
                recipient_list=[user.email],
                fail_silently=False
            )
        user.save()
        return user.to_dict()


class UserLogoutView(View):
    @require_logged_in
    def post(self, request) -> Any:
        logout(request)
        return


class UserValidateView(View):
    def post(self, request) -> Any:
        self.check_input(['token'])
        token = request.data.get('token')
        decoded = base64.urlsafe_b64decode(token).decode()
        username, email = decoded.split('&')
        user = User.objects.get(username=username)
        m = hashlib.md5()
        m.update((user.email + VALIDATE_SALT).encode('utf-8'))
        if m.hexdigest() == email:
            user.is_active = True
            user.save()
            return
        raise Exception('email validation failed')
