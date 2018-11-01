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
