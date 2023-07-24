from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    body = models.TextField(blank=False)
    date_created = models.DateTimeField(auto_now=False, blank=False)
    colours = [
        ('#34ccff', 'blue-theme'),
        ('#e4f78f', 'green-theme'),
        ('#ffc983', 'orange-theme'),
        ('#ffa0a1', 'red-theme'),
        ('#b99aff', 'purple-theme')
    ]
    note_colour = models.TextField(choices=colours, max_length=7, blank=False, null=False)

    def __str__(self):
        return f"{self.user.username} - {self.body[:30]}"
    
    def is_new(self):
        if self.date_created.day == timezone.now().day:
            return True
        else:
            return False