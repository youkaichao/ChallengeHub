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
            raise Exception('用户名或密码错误！')
        else:
            raise Exception('用户还未激活，请检查邮箱或联系管理员。')


class UserInfoView(View):
    @require_logged_in
    def get(self, request) -> Any:
        return request.user.to_dict()

    @require_logged_in
    def post(self, request) -> Any:
        for name in ['introduction', 'school']:
            if request.data.get(name) is not None:
                setattr(request.user, name, request.data.get(name))
        request.user.save()
        return request.user.to_dict()


class UserRegisterView(View):
    def post(self, request) -> Any:
        self.check_input(['username', 'password', 'email', 'individual'])
        user = User.objects.filter(username=request.data.get('username'))
        if user:
            raise Exception('用户名已经存在！')
        if User.objects.filter(email=request.data.get('email')):
            raise Exception('邮箱已经被注册！')
        individual=True if (request.data.get('individual') == 'individual') else False
        user = User.objects.create_user(
            username=request.data.get('username'),
            password=request.data.get('password'),
            email=request.data.get('email'),
            individual=individual,
            is_active=individual and not USE_MAIL_VALIDATE
        )
        m = hashlib.md5()
        m.update((user.email + VALIDATE_SALT).encode('utf-8'))
        encoded = base64.urlsafe_b64encode(
            f'{user.username}&{m.hexdigest()}'.encode('utf-8'))
        link = f'http://{SITE_URL}/#/validate/{encoded.decode()}'
        if USE_MAIL_VALIDATE:
            send_mail(
                subject='验证你在 ChanllengeHub 上的账号',
                message=f'{user.username}， 请点击以下链接验证你的账户：\n{link}',
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
        raise Exception('邮箱验证失败！')

        
class UserResetPasswdView(View):
    @require_logged_in
    def post(self, request) -> Any:
        self.check_input(['old', 'new'])
        old = request.data.get('old')
        new = request.data.get('new')
        user = authenticate(username=request.user.username, password=old)
        if not user:
            raise Exception('密码错误！')
        user.set_password(new)
        user.save()
        login(request, user)