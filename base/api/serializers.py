from rest_framework.serializers import ModelSerializer
from base.models import Task

class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'user', 'header', 'description', 'date_created', 'due_date', 'is_new', 'urgency', 'task_colour', 'completed']