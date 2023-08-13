from rest_framework.serializers import ModelSerializer
from base.models import Task

class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'body', 'date_created', 'is_new', 'task_colour', 'completed']