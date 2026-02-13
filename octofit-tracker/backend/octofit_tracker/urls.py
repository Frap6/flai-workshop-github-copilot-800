"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
import os
from .views import UserViewSet, TeamViewSet, ActivityViewSet, LeaderboardViewSet, WorkoutViewSet

# Get codespace environment variable
codespace_name = os.environ.get('CODESPACE_NAME')
if codespace_name:
    base_url = f"https://{codespace_name}-8000.app.github.dev"
else:
    base_url = "http://localhost:8000"

# Create a router and register viewsets
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'teams', TeamViewSet, basename='team')
router.register(r'activities', ActivityViewSet, basename='activity')
router.register(r'leaderboard', LeaderboardViewSet, basename='leaderboard')
router.register(r'workouts', WorkoutViewSet, basename='workout')


@api_view(['GET'])
def api_root(request):
    """
    API root endpoint that lists all available endpoints
    """
    return Response({
        'message': 'Welcome to OctoFit Tracker API',
        'base_url': base_url,
        'endpoints': {
            'users': request.build_absolute_uri(reverse('user-list')),
            'teams': request.build_absolute_uri(reverse('team-list')),
            'activities': request.build_absolute_uri(reverse('activity-list')),
            'leaderboard': request.build_absolute_uri(reverse('leaderboard-list')),
            'workouts': request.build_absolute_uri(reverse('workout-list')),
            'admin': request.build_absolute_uri('/admin/'),
        }
    })


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api_root, name='api-root'),
    path('api/', api_root, name='api-root-alt'),
    path('api/', include(router.urls)),
]
