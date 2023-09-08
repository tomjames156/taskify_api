from rest_framework import serializers
from django.contrib.auth.models import User
from base.models import Task, UserProfile

class ProfilePicSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['profile_pic']

    def save(self, *args, **kwargs):
        if self.instance.profile_pic:
            self.instance.profile_pic.delete()
            return super().save(*args, **kwargs)

class ProfileTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'header']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class SimpleProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = UserProfile

        fields = ['profile_pic', 'username']
        extra_kwargs = {'email': {'required': False}, 'firstname': {'required': False}}

class TaskSerializer(serializers.ModelSerializer):
    user_profile = SimpleProfileSerializer(many=False, read_only=True)
    

    class Meta:
        model = Task
        fields = ['id', 'user', 'user_profile', 'header', 'description', 'date_created', 'due_date', 'last_updated', 'is_new', 'urgency', 'task_colour', 'completed']
        extra_kwargs = {'user': {'required': False}, 'date_created': {'required': False} }


class TaskNumbersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id']


class ProfileSerializer(serializers.ModelSerializer):
    tasks = ProfileTaskSerializer(source='user.tasks', many=True, read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    firstname = serializers.CharField(source='user.first_name', read_only=True)
    lastname = serializers.CharField(source='user.last_name', read_only=True)
    date_joined = serializers.DateTimeField(source='user.date_joined', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=False)

    class Meta:
        model = UserProfile
        fields = ['username', 'firstname', 'lastname', 'bio', 'profile_pic', 'date_joined', 'email', 'location', 'tasks', 'email_confirmed']

        extra_kwargs = {'email': {'required': False}, 'firstname': {'required': False}}


class SimpleUserProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    firstname = serializers.CharField(source='user.first_name', read_only=True)
    lastname = serializers.CharField(source='user.last_name', read_only=True)
    date_joined = serializers.DateTimeField(source='user.date_joined', read_only=True)
    tasks = TaskNumbersSerializer(source="user.tasks", many=True, read_only=True)

    class Meta:
        model = UserProfile
        fields = ['username', 'firstname', 'lastname', 'bio', 'profile_pic', 'location', 'tasks', 'date_joined']

class PublicProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    email = serializers.EmailField(source="user.email", read_only=True)
    firstname = serializers.CharField(source='user.first_name', read_only=True)
    lastname = serializers.CharField(source="user.last_name", read_only=True)
    date_joined = serializers.CharField(source="user.date_joined", read_only=True)

    class Meta:
        model = UserProfile

        fields = ['username', 'firstname', 'lastname', 'email', 'date_joined', 'profile_pic', 'bio', 'location']