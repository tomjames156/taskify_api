from django.urls import path
from .views import *


from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('', get_routes, name='get_routes'),
    path('tasks/', all_tasks, name='all_tasks' ),
    path('tasks/completed/', completed_tasks, name='completed_tasks'),
    path('tasks/new/', new_tasks, name="new_tasks"),
    path('tasks/incomplete/', incomplete_tasks, name='incomplete_tasks'),
    path('tasks/recent/', recent_tasks, name='recent_tasks'),
    path('tasks/urgency/', tasks_urgency, name='tasks_urgency'),
    path('task/<str:pk>', task_details, name='task_details'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile', user_profile, name="user_profile")
]
