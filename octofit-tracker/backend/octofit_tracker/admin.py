from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Admin configuration for User model"""
    list_display = ['username', 'email', 'full_name', 'team', 'created_at']
    list_filter = ['team', 'created_at']
    search_fields = ['username', 'email', 'full_name']
    ordering = ['-created_at']


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    """Admin configuration for Team model"""
    list_display = ['name', 'captain', 'total_points', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'captain']
    ordering = ['-total_points']


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    """Admin configuration for Activity model"""
    list_display = ['user', 'activity_type', 'duration', 'distance', 'calories', 'points', 'date']
    list_filter = ['activity_type', 'date', 'created_at']
    search_fields = ['user', 'activity_type']
    ordering = ['-date']


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    """Admin configuration for Leaderboard model"""
    list_display = ['rank', 'user', 'team', 'total_points', 'total_activities', 'last_updated']
    list_filter = ['team', 'last_updated']
    search_fields = ['user', 'team']
    ordering = ['rank']


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    """Admin configuration for Workout model"""
    list_display = ['name', 'difficulty', 'duration', 'category', 'created_at']
    list_filter = ['difficulty', 'category', 'created_at']
    search_fields = ['name', 'category', 'recommended_for']
    ordering = ['difficulty', 'name']
