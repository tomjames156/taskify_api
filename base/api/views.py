from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.views import APIView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
# import FileUploadParser


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


from base.models import Task
from .serializers import ProfilePicSerializer, SimpleUserProfileSerializer, UserSerializer

from django.contrib import messages
from datetime import timedelta, datetime
from django.utils import timezone

from .utils import *

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email

        return token
    
    default_error_messages =  {'no_active_account': 'Username or Password is incorrect'}


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET'])
def get_routes(request):
    routes = ['/api/token', '/api/token/refresh', '/api/tasks', '/api/tasks/completed', '/api/tasks/recent', '/api/tasks/incomplete']
    return Response(routes)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def all_tasks(request):
    if request.method == 'GET':
        return get_all_tasks(request)
    elif request.method == 'POST':
        return create_task(request)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def completed_tasks(request):
    return get_completed_tasks(request)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def new_tasks(request):
    return get_new_tasks(request)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recent_tasks(request):
    return get_recent_tasks(request)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def incomplete_tasks(request):
    return get_incomplete_tasks(request)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def tasks_urgency(request):
    return get_tasks_urgency(request)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def task_details(request, pk):
    if request.method == 'GET':
        return get_task(request, pk)
    elif request.method == 'PUT':
        return update_task(request, pk)
    elif request.method == 'DELETE':
        return delete_task(request, pk)
    

@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def user_profile(request):
    if request.method == 'GET':
        return get_user_profile(request)
    elif request.method == 'PUT':
        return update_user_profile(request)


class ProfilePicUpload(APIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        curr_user_profile = UserProfile.objects.get(user=request.user)
        serializer = ProfilePicSerializer(data=request.data, instance=curr_user_profile)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST', 'PUT'])
@permission_classes([IsAuthenticated])
def get_users(request):
    if request.method == 'GET':
        return users(request)
    elif request.method == 'POST':
        return create_user(request)
    elif request.method == 'PUT':
        return search_users(request)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_public_profile(request, username):
    if request.method == 'GET':
        return user_public_profile(request, username)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user(request, pk):
    if request.method == 'GET':
        return user(request, pk)
