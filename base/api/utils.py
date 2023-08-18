from base.models import Task
from .serializers import TaskSerializer
from .views import *

from django.utils import timezone
from django.contrib.auth.models import User

from datetime import timedelta, datetime

from rest_framework import status
from rest_framework.response import Response

default_user = User.objects.get(username="t0m1")
tomorrow = timezone.now() + timedelta(days=1)


def get_all_tasks(request):
    tasks = Task.objects.filter(user=default_user, date_created__lte=timezone.now()).order_by('-date_created')
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


def get_tasks_urgency(request):
    tasks = Task.objects.filter(user=request.user, completed=False).order_by('due_date')
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


def get_task(request, pk):
    task = Task.objects.get(pk=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)


def create_task(request):
    data = request.data
    task = Task.objects.create(user=default_user, date_created=timezone.now(), due_date=tomorrow, header=data['header'], description=data['description'])
    serializer = TaskSerializer(instance=task, many=False)
    return Response(serializer.data)


def update_task(request, pk):
    task = Task.objects.get(pk=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def delete_task(request, pk):
    Task.objects.get(pk=pk).delete()    
    return Response('Successfully deleted')

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


# todo add image field to the user model