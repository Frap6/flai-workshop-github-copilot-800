from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model"""
    id = serializers.CharField(read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password', 'full_name', 'team', 'avatar_url', 'created_at']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        """Create a new user with encrypted password"""
        user = User(**validated_data)
        user.save()
        return user

    def to_representation(self, instance):
        """Convert ObjectId to string"""
        representation = super().to_representation(instance)
        if hasattr(instance, 'id'):
            representation['id'] = str(instance.id)
        return representation


class TeamSerializer(serializers.ModelSerializer):
    """Serializer for Team model"""
    id = serializers.CharField(read_only=True)
    
    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'captain', 'members', 'total_points', 'created_at']

    def to_representation(self, instance):
        """Convert ObjectId to string"""
        representation = super().to_representation(instance)
        if hasattr(instance, 'id'):
            representation['id'] = str(instance.id)
        return representation


class ActivitySerializer(serializers.ModelSerializer):
    """Serializer for Activity model"""
    id = serializers.CharField(read_only=True)
    
    class Meta:
        model = Activity
        fields = ['id', 'user', 'activity_type', 'duration', 'distance', 'calories', 'points', 'date', 'notes', 'created_at']

    def to_representation(self, instance):
        """Convert ObjectId to string"""
        representation = super().to_representation(instance)
        if hasattr(instance, 'id'):
            representation['id'] = str(instance.id)
        return representation


class LeaderboardSerializer(serializers.ModelSerializer):
    """Serializer for Leaderboard model"""
    id = serializers.CharField(read_only=True)
    
    class Meta:
        model = Leaderboard
        fields = ['id', 'user', 'team', 'total_points', 'total_activities', 'rank', 'last_updated']

    def to_representation(self, instance):
        """Convert ObjectId to string"""
        representation = super().to_representation(instance)
        if hasattr(instance, 'id'):
            representation['id'] = str(instance.id)
        return representation


class WorkoutSerializer(serializers.ModelSerializer):
    """Serializer for Workout model"""
    id = serializers.CharField(read_only=True)
    
    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'difficulty', 'duration', 'category', 'exercises', 'recommended_for', 'created_at']

    def to_representation(self, instance):
        """Convert ObjectId to string"""
        representation = super().to_representation(instance)
        if hasattr(instance, 'id'):
            representation['id'] = str(instance.id)
        return representation
