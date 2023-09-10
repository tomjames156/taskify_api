from django.contrib import admin
from .models import Task, UserProfile, UserFriending


admin.site.register(Task)
admin.site.register(UserProfile)
admin.site.register(UserFriending)