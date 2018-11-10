import json
from django.views.generic import View
from django.http import JsonResponse


def check_input(query, names):
    for name in names:
        if query.get(name) == None:
            return False
    return True


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
        request.data = {}
        if request.method == 'GET':
            request.data = request.GET.dict()
        elif request.content_type == 'application/json':
            request.data = json.loads(request.body)
        return self.do_dispatch(request, *args, **kwargs)

    def do_dispatch(self, *args, **kwargs):
        handler = getattr(self, self.request.method.lower(), None)
        if not callable(handler):
            return self.http_method_not_allowed()
        else:
            return handler(*args, **kwargs)
