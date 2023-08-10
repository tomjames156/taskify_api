from django.urls import path
from .views import *


from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('', get_routes, name='get routes'),
    path('notes/', get_tasks, name='get notes' ),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
]
