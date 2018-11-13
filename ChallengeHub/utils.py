import json
import traceback
from django.views.generic import View
from django.http import JsonResponse


def make_errors(msg):
    if msg:
        return {'error': msg, 'code': 1}
    else:
        return {'code': 0}


def require_logged_in(func):
    def new_func(self, request):
        if not request.user.is_authenticated():
            return JsonResponse(make_errors('not logged in'))
        else:
            return func(self, request)
    return new_func


class BaseView(View):
    def dispatch(self, request, *args, **kwargs):
        self.request = request
        request.data = {}
        if request.method == 'GET':
            request.data = request.GET.dict()
        elif request.content_type == 'application/json':
            request.data = json.loads(request.body)
        else:
            request.data = request.body
        return self.do_dispatch(request, *args, **kwargs)

    def do_dispatch(self, *args, **kwargs):
        handler = getattr(self, self.request.method.lower(), None)
        if not callable(handler):
            return JsonResponse(make_errors(f"http method {self.request.method.lower()} not allowed "))
        else:
            try:
                return handler(*args, **kwargs)
            except Exception as e:
                traceback.print_exc()
                return JsonResponse(make_errors(str(e)))

    def check_input(self, names):
        missing_names = [name for name in names if self.request.data.get(name) == None]
        if missing_names:
            raise Exception(f"missing input(s): {missing_names}")