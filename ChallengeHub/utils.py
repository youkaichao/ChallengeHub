import json
import typing
import traceback
from django.views.generic import View
from django.http import JsonResponse
from typing import Dict, Any, Callable, List
from basic.models import Competition
from django.test import Client
from useraction.models import User
from django.db.models import Model


def delete_table(model: typing.Type[Model]):
    for q in model.objects.all():
        q.delete()


class MyClient(Client):

    def get(self, *args, **kwargs):
        response = super(MyClient, self).get(*args, **kwargs)
        return json.loads(response.content.decode())

    def post(self, *args, **kwargs):
        # 对于post来说，默认类型要是json
        if 'content_type' not in kwargs:
            kwargs['content_type'] = 'application/json'
        if 'data' in kwargs and kwargs.get('content_type') == 'application/json':
            kwargs['data'] = json.dumps(kwargs['data'])
        response = super(MyClient, self).post(*args, **kwargs)
        return json.loads(response.content.decode())

    def put(self, *args, **kwargs):
        kwargs['content_type'] = 'application/json'
        response = super(MyClient, self).put(*args, **kwargs)
        return json.loads(response.content.decode())

    def patch(self, *args, **kwargs):
        kwargs['content_type'] = 'application/json'
        response = super(MyClient, self).patch(*args, **kwargs)
        return json.loads(response.content.decode())

    def delete(self, *args, **kwargs):
        kwargs['content_type'] = 'application/json'
        response = super(MyClient, self).delete(*args, **kwargs)
        return json.loads(response.content.decode())


def make_errors(msg: str) -> Dict[str, Any]:
    return {'error': msg, 'code': 1}


def require_logged_in(func: Callable[..., Any]) -> Callable[..., Any]:
    def new_func(self, request, *args, **kwargs) -> Any:
        if not request.user.is_authenticated():
            raise Exception('用户未登录！')
        else:
            return func(self, request, *args, **kwargs)

    return new_func


def require_to_be_organization(func: Callable[..., Any]) -> Callable[..., Any]:
    def new_func(self, request, *args, **kwargs) -> Any:
        if request.user.individual:
            raise Exception('该账号是个人账号，请使用机构账号访问。')
        else:
            return func(self, request, *args, **kwargs)

    return new_func


def require_to_be_individual(func: Callable[..., Any]) -> Callable[..., Any]:
    def new_func(self, request, *args, **kwargs) -> Any:
        if not request.user.individual:
            raise Exception('该账号是机构账号，请使用个人账号访问。')
        else:
            return func(self, request, *args, **kwargs)

    return new_func


def require_to_be_publisher(func: Callable[..., Any]) -> Callable[..., Any]:
    def new_func(self, request, *args, **kwargs) -> Any:
        if 'contest_id' in kwargs:
            contest_id = kwargs['contest_id']
            contest = Competition.objects.get(id=int(contest_id))
            if contest.publisher != request.user:
                raise Exception(f'你不是该比赛{contest.name}的主办方！')
        return func(self, request, *args, **kwargs)

    return new_func


class BaseView(View):
    def dispatch(self, request, *args, **kwargs) -> JsonResponse:
        self.request = request
        request.data = {}
        if request.method == 'GET':
            request.data = request.GET.dict()
        elif request.content_type == 'application/json':
            request.data = request.body.replace(b"'", b'"')
            request.data = json.loads(request.data or '{}')
        elif request.content_type == 'multipart/form-data':
            request.data = request.POST.dict()
            request.data['file'] = request.FILES['file']
        return self.do_dispatch(request, *args, **kwargs)

    def do_dispatch(self, *args, **kwargs) -> JsonResponse:
        handler = getattr(self, self.request.method.lower(), None)
        if not callable(handler):
            return JsonResponse(make_errors(f"http method {self.request.method.lower()} not allowed "))
        else:
            try:
                data = handler(*args, **kwargs)
                if data is None:
                    data = 'success'
                return JsonResponse({'data': data, 'code': 0})
            except Exception as e:
                traceback.print_exc()
                return JsonResponse(make_errors(str(e)))

    def check_input(self, names: List[str]) -> None:
        missing_names = [
            name for name in names if self.request.data.get(name) == None]
        if missing_names:
            raise Exception(f"missing input(s): {missing_names}")
