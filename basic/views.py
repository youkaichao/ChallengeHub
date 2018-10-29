from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from .models import Competition
import json
# Create your views here.


@csrf_exempt
def add_competition(request):
    response = {}
    print(request.POST)
    try:
        competition = Competition(
            name=request.POST.get('name'), subject=request.POST.get('subject'))
        competition.save()
        response['msg'] = 'success'
        response['err'] = 0
    except Exception as e:
        response['msg'] = str(e)
        print(str(e))
        response['err'] = 1
    return JsonResponse(response)


@csrf_exempt
def show_competition(request):
    response = {}
    try:
        competitions = Competition.objects.all()
        response['list'] = json.loads(
            serializers.serialize("json", competitions))
        response['msg'] = 'success'
        response['err'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['err'] = 1

    return JsonResponse(response)
