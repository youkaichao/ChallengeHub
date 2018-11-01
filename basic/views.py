from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.views.generic import View
from django.core import serializers
from basic.models import Competition
from useraction.models import User
from ChallengeHub.utils import *


class ContestView(View):
    def get(self, request):
        if(not check_input(request.GET, ['id'])):
            competitions = Competition.objects.all()
            return JsonResponse({'code': 0, "data": serializers.serialize('json', competitions)})
        try:
            c = Competition.objects.get(id=request.GET.get('id'))
            info = {
                'name': c.name,
                'subject': c.subject,
                'groupSize': c.group_size,
                'enrollStart': c.enroll_start,
                'enrollEnd': c.enroll_end,
                'detail': c.detail,
                'procedure': c.procedure,
                'url': c.url,
                'charge': c.charge,
                'upvote': c.upvote,
                'downvote': c.downvote,
                'publisher': c.publisher.username
            }
            return JsonResponse({'code': 0, 'data': info})
        except Exception as e:
            return JsonResponse(make_errors(str(e)))

    def post(self, request):
        if(not check_input(request.POST, ['name', 'subject', 'groupSize', 'enrollStart', 'enrollEnd', 'detail', 'procedure', 'url', 'charge', 'publisher'])):
            return JsonResponse(make_errors('invalid input'))
        c = Competition(
            name=request.POST.get('name'),
            subject=request.POST.get('subject'),
            group_size=request.POST.get('groupSize'),
            enroll_start=request.POST.get('enrollStart'),
            enroll_end=request.POST.get('enrollEnd'),
            detail=request.POST.get('detail'),
            procedure=request.POST.get('procedure'),
            url=request.POST.get('url'),
            charge=request.POST.get('charge'),
        )
        try:
            p = User.objects.get(username=request.POST.get('publisher'))
            c.publisher = p
            c.save()
        except Exception as e:
            return JsonResponse(make_errors(str(e)))
        return JsonResponse({'code': 0, 'data': 'Success'})
