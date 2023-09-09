from base.models import Task, UserProfile
from .serializers import TaskSerializer, ProfileSerializer, SimpleUserProfileSerializer, PublicProfileSerializer
from .views import *

from django.utils import timezone
from django.contrib.auth.models import User

from datetime import timedelta, datetime

from rest_framework import status
from rest_framework.response import Response

from django.core.mail import send_mail
from backend.settings import *

import re

default_user = User.objects.get(username="t0m1")
tomorrow = timezone.now() + timedelta(days=1)


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


def get_tasks_urgency(request):
    tasks = Task.objects.filter(user=request.user, completed=False).order_by('due_date')
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


def get_task(request, pk):
    try:
        task = Task.objects.get(pk=pk, user=request.user)
        serializer = TaskSerializer(task, many=False)
        return Response(serializer.data)
    except(Task.DoesNotExist, ValueError):
        content = {'Task Not Found': 'Task Does Not Exist'}
        return Response(content, status=status.HTTP_404_NOT_FOUND)



def create_task(request):
    data = request.data
    user = User.objects.get(username=request.user.username)
    if data['due_date'] != '':
        task = Task.objects.create(user=user, date_created=timezone.now(), description=data['description'], due_date=data['due_date'], header=data['header'], task_colour=data['task_colour'], completed=data['completed'])
        task.user_profile = UserProfile.objects.get(user=user)
        task.save()
    else:
        task = Task.objects.create(user=user, date_created=timezone.now(), description=data['description'], header=data['header'], task_colour=data['task_colour'], completed=data['completed'])
        task.user_profile = UserProfile.objects.get(user=user)
        task.save()
    serializer = TaskSerializer(instance=task, many=False)
    return Response(serializer.data)


def update_task(request, pk):
    task = Task.objects.get(user=request.user, pk=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def delete_task(request, pk):
    Task.objects.get(user=request.user, pk=pk).delete()    
    return Response('Successfully deleted')


def get_user_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    serializer = ProfileSerializer(user_profile, many=False)
    return Response(serializer.data)

def update_user_profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        user_profile.bio = request.data['bio']
        user_profile.user.first_name = request.data['firstname']
        user_profile.user.last_name = request.data['lastname']
        user_profile.user.email = request.data['email']
        user_profile.location = request.data['location']
        user_profile.save()
        serializer = ProfileSerializer(user_profile, many=False)
        return Response(serializer.data)
    except (UserProfile.DoesNotExist, ValueError): 
        content = {'Failed Profile Update': 'Profile not updated'}
        return Response(content, status=status.HTTP_404_NOT_FOUND)


def users(request):
    users = UserProfile.objects.all()
    serializer = SimpleUserProfileSerializer(users, many=True)
    return Response(serializer.data)


def user(request, pk):
    user = UserProfile.objects.get(pk=pk)
    serializer = SimpleUserProfileSerializer(user, many=False)
    return Response(serializer.data)


def create_user(request):
    # todo - Add an option to sign in as a guest by creating a guest account and logging into it. But don't allow following on the guest account
    data = request.data
    new_user = User.objects.create_user(username=data['username'].lower(), first_name=data['firstname'], last_name=data['lastname'], email=data['email'], password=data['password1'])
    UserProfile.objects.create(user=new_user, email_confirmed=False)
    send_mail("Taskify App", "Welcome to the Taskify App by Tomi.co. \nManage all your tasks efficiently and let others send tasks to you🙂.", EMAIL_HOST_USER, recipient_list=[new_user.email], fail_silently=False)
    return Response('Account Successfully created')


def search_users(request):
    data = request.data
    query = data['query']
    search_matches = []
    searchRegex = re.compile(rf"^{query}.*")
    all_user_profiles = UserProfile.objects.all()
    for user_profile in all_user_profiles:
        if searchRegex.findall(user_profile.user.username) != []:
            search_matches.append(user_profile)
    serializer = SimpleUserProfileSerializer(search_matches, many=True)
    return Response(serializer.data)


def user_public_profile(request, username):
    try:
        user = User.objects.get(username=username)
        profile = UserProfile.objects.get(user=user)
        serializer = PublicProfileSerializer(profile, many=False)
        return Response(serializer.data)
    except (User.DoesNotExist, UserProfile.DoesNotExist, ValueError):
        content = {'User Not Found': 'Username not registered'}
        return Response(content, status=status.HTTP_404_NOT_FOUND)
    

# def send_email(request):


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