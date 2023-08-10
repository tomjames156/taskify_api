from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


from base.models import Task
from .serializers import TaskSerializer

from django.contrib import messages


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
    routes = ['/api/token', '/api/token/refresh', '/api/tasks']
    return Response(routes)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_tasks(request):
    user = request.user
    tasks = Task.objects.filter(user=user).order_by('-date_created')
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)