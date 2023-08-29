from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

import datetime
from dateutil import parser

import os

tomorrow = timezone.now() + datetime.timedelta(days=1)

def upload_to(instance, filename):
    now = timezone.now()
    base, extension = os.path.splitext(filename.lower())
    milliseconds = now.microsecond // 1000
    return f"users/{instance.pk}/{now:%Y%m%d%H%M%S}{milliseconds}{extension}"

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_profile')
    bio = models.CharField(max_length=200, blank=True)
    profile_pic = models.ImageField(upload_to=upload_to, blank=True, default='no_pfp.jpeg')
    location = models.CharField(max_length=150, blank=True)
    
    def __str__(self):
        return f"{self.user.username}'s profile"


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_profile', null=True)
    header = models.TextField(blank=True)
    description = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now=False, blank=False, null=False)
    due_date = models.DateTimeField(default=tomorrow, blank=False, null=False)
    last_updated = models.DateTimeField(auto_now=True)
    colours = [
        ('#34ccff', 'blue-theme'),
        ('#e4f78f', 'green-theme'),
        ('#ffc983', 'orange-theme'),
        ('#ffa0a1', 'red-theme'),
        ('#b99aff', 'purple-theme')
    ]
    task_colour = models.TextField(choices=colours, default='#ffc983', max_length=7, blank=False, null=False)
    completed = models.BooleanField(default=False, null=False, blank=False)

    def __str__(self):
        return f"{self.user.username} - {self.header[:30]}"
    
    def is_new(self):
        if ((self.date_created.day == timezone.now().day) and (self.completed == False)):
            return True
        else:
            return False
    
    def urgency(self):
        if (self.completed == False) and (parser.parse(str(self.due_date)) > timezone.now()):
            diff = self.due_date - timezone.now()
            if diff.days == 0:
                return 1
            elif diff.days == 1:
                return 2
            elif diff.days == 2:
                return 3
            elif diff.days >= 3:
                return 4
        elif (self.completed == False) and (parser.parse(str(self.due_date)) < timezone.now()):
            return 0
        elif self.completed == True:
            return 5


# class Friend(models.Model):
#     """Represents a friend of a user"""
#     friend_user = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
#     friending_user = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
#     date_friended = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         unique_together = ('friend_user', 'friending_user')

#     def __str__(self):
#         return f"{self.friend_user} {self.friending_user}"