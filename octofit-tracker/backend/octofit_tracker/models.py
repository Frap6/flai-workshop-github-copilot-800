from django.db import models
from django.contrib.auth.models import AbstractUser


class User(models.Model):
    """User model for OctoFit Tracker"""
    email = models.EmailField(unique=True, max_length=255)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    team = models.CharField(max_length=100, blank=True, null=True)
    avatar_url = models.CharField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'users'
        indexes = [
            models.Index(fields=['email']),
        ]

    def __str__(self):
        return self.username


class Team(models.Model):
    """Team model for OctoFit Tracker"""
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    captain = models.CharField(max_length=150)
    members = models.JSONField(default=list)
    total_points = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'teams'

    def __str__(self):
        return self.name


class Activity(models.Model):
    """Activity model for OctoFit Tracker"""
    user = models.CharField(max_length=150)
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField(help_text="Duration in minutes")
    distance = models.FloatField(default=0.0, help_text="Distance in kilometers")
    calories = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    date = models.DateTimeField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'activities'
        ordering = ['-date']

    def __str__(self):
        return f"{self.user} - {self.activity_type} - {self.date}"


class Leaderboard(models.Model):
    """Leaderboard model for OctoFit Tracker"""
    user = models.CharField(max_length=150, unique=True)
    team = models.CharField(max_length=100)
    total_points = models.IntegerField(default=0)
    total_activities = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'leaderboard'
        ordering = ['-total_points']

    def __str__(self):
        return f"{self.rank}. {self.user} - {self.total_points} points"


class Workout(models.Model):
    """Workout model for OctoFit Tracker"""
    name = models.CharField(max_length=255)
    description = models.TextField()
    difficulty = models.CharField(max_length=50)
    duration = models.IntegerField(help_text="Duration in minutes")
    category = models.CharField(max_length=100)
    exercises = models.JSONField(default=list)
    recommended_for = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'workouts'

    def __str__(self):
        return f"{self.name} ({self.difficulty})"
