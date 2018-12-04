import json
import traceback
from django.views.generic import View
from django.http import JsonResponse
from typing import Dict, Any, Callable, List
from basic.models import Competition


def make_errors(msg: str) -> Dict[str, Any]:
    return {'error': msg, 'code': 1}


def require_logged_in(func: Callable[..., Any]) -> Callable[..., Any]:
    def new_func(self, request, *args, **kwargs) -> Any:
        if not request.user.is_authenticated():
            raise Exception('not logged in')
        else:
            return func(self, request, *args, **kwargs)

    return new_func
    
    
def require_to_be_organization(func: Callable[..., Any]) -> Callable[..., Any]:
    def new_func(self, request, *args, **kwargs) -> Any:
        if request.user.individual:
            raise Exception('your account is an individual account')
        else:
            return func(self, request, *args, **kwargs)

    return new_func
    
    
def require_to_be_individual(func: Callable[..., Any]) -> Callable[..., Any]:
    def new_func(self, request, *args, **kwargs) -> Any:
        if not request.user.individual:
            raise Exception('your account is an organization account')
        else:
            return func(self, request, *args, **kwargs)

    return new_func
    
    
def require_to_be_publisher(func: Callable[..., Any]) -> Callable[..., Any]:
    def new_func(self, request, *args, **kwargs) -> Any:
        if 'contest_id' in kwargs:
            contest_id = kwargs['contest_id']
            contest = Competition.objects.get(id=int(contest_id))
            if (contest.publisher != request.user):
                raise Exception('no authority to change stage')
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
