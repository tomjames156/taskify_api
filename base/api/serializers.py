from rest_framework.serializers import ModelSerializer
from base.models import Task

class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'user', 'header', 'description', 'date_created', 'due_date', 'last_updated', 'is_new', 'urgency', 'task_colour', 'completed']
        extra_kwargs = {'user': {'required': False}, 'date_created': {'required': False} }