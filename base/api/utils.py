from base.models import Task
from .serializers import TaskSerializer
from .views import *

from django.utils import timezone
from django.contrib.auth.models import User

from datetime import timedelta, datetime

from rest_framework.response import Response
default_user = User.objects.get(username="t0m1")


def get_all_tasks(request):
    tasks = Task.objects.filter(user=request.user, date_created__lte=timezone.now()).order_by('-date_created')
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


def get_completed_tasks(request):
    tasks = Task.objects.filter(user=request.user, date_created__lte=timezone.now(), completed=True).order_by('-date_created')
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


def get_new_tasks(request):
    today = timezone.now()
    today_midnight = datetime(today.year, today.month, today.day, 0, 0, 0, tzinfo=today.tzinfo)
    tasks = Task.objects.filter(user=request.user, date_created__gte=today_midnight, completed=False).order_by('-date_created')
    tasks = tasks.filter(date_created__lte=timezone.now())
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


def get_recent_tasks(request):
    today = timezone.now()
    yesterday = datetime(today.year, today.month, today.day, 0, 0, 0, tzinfo=today.tzinfo)
    yesterday = yesterday + timedelta(days=-1)
    tasks = Task.objects.filter(user=request.user, date_created__gte=yesterday).order_by('-date_created')
    tasks = tasks.filter(date_created__lte=timezone.now())
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


def get_incomplete_tasks(request):
    tasks = Task.objects.filter(user=request.user, completed=False, date_created__lte=timezone.now()).order_by('-date_created')
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


api_routes = [
    {
        'Endpoint': '/token/',
        'method': 'POST',
        'body': {
            'username: ""', 
            'password: ""'
        },
        'description': 'Returns an array of notes'
    }
]