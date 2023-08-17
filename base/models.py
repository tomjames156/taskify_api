from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from datetime import timedelta

tomorrow = timezone.now() + timedelta(days=1)

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    header = models.TextField(blank=False)
    description = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now=False, blank=False)
    due_date = models.DateTimeField(default=tomorrow, blank=False, null=False)
    colours = [
        ('#34ccff', 'blue-theme'),
        ('#e4f78f', 'green-theme'),
        ('#ffc983', 'orange-theme'),
        ('#ffa0a1', 'red-theme'),
        ('#b99aff', 'purple-theme')
    ]
    task_colour = models.TextField(choices=colours, max_length=7, blank=False, null=False)
    completed = models.BooleanField(default=False, null=False, blank=False)

    def __str__(self):
        return f"{self.user.username} - {self.body[:30]}"
    
    def is_new(self):
        if ((self.date_created.day == timezone.now().day) and (self.completed == False)):
            return True
        else:
            return False
    
    def urgency(self):
        if (self.completed == False) and (self.due_date > timezone.now()):
            diff = self.due_date - timezone.now()
            if diff.days == 0:
                return 1
            elif diff.days == 1:
                return 2
            elif diff.days == 2:
                return 3
            elif diff.days >= 3:
                return 4
        elif (self.completed == False) and (self.due_date < timezone.now()):
            return 0
        elif self.completed == True:
            return 5