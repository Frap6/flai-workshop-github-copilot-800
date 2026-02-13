from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from datetime import datetime
from .models import User, Team, Activity, Leaderboard, Workout


class UserModelTest(TestCase):
    """Test cases for User model"""
    
    def setUp(self):
        """Set up test data"""
        self.user = User.objects.create(
            email='test@example.com',
            username='testuser',
            password='testpass123',
            full_name='Test User',
            team='Team Alpha'
        )
    
    def test_user_creation(self):
        """Test that a user can be created"""
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertEqual(self.user.team, 'Team Alpha')
    
    def test_user_str(self):
        """Test the string representation of user"""
        self.assertEqual(str(self.user), 'testuser')


class TeamModelTest(TestCase):
    """Test cases for Team model"""
    
    def setUp(self):
        """Set up test data"""
        self.team = Team.objects.create(
            name='Team Alpha',
            description='Test team',
            captain='testuser',
            members=['user1', 'user2'],
            total_points=100
        )
    
    def test_team_creation(self):
        """Test that a team can be created"""
        self.assertEqual(self.team.name, 'Team Alpha')
        self.assertEqual(self.team.captain, 'testuser')
        self.assertEqual(self.team.total_points, 100)
    
    def test_team_str(self):
        """Test the string representation of team"""
        self.assertEqual(str(self.team), 'Team Alpha')


class ActivityModelTest(TestCase):
    """Test cases for Activity model"""
    
    def setUp(self):
        """Set up test data"""
        self.activity = Activity.objects.create(
            user='testuser',
            activity_type='Running',
            duration=30,
            distance=5.0,
            calories=300,
            points=50,
            date=datetime.now(),
            notes='Morning run'
        )
    
    def test_activity_creation(self):
        """Test that an activity can be created"""
        self.assertEqual(self.activity.user, 'testuser')
        self.assertEqual(self.activity.activity_type, 'Running')
        self.assertEqual(self.activity.duration, 30)
        self.assertEqual(self.activity.distance, 5.0)


class LeaderboardModelTest(TestCase):
    """Test cases for Leaderboard model"""
    
    def setUp(self):
        """Set up test data"""
        self.entry = Leaderboard.objects.create(
            user='testuser',
            team='Team Alpha',
            total_points=500,
            total_activities=10,
            rank=1
        )
    
    def test_leaderboard_creation(self):
        """Test that a leaderboard entry can be created"""
        self.assertEqual(self.entry.user, 'testuser')
        self.assertEqual(self.entry.total_points, 500)
        self.assertEqual(self.entry.rank, 1)


class WorkoutModelTest(TestCase):
    """Test cases for Workout model"""
    
    def setUp(self):
        """Set up test data"""
        self.workout = Workout.objects.create(
            name='Beginner Cardio',
            description='Great for beginners',
            difficulty='Easy',
            duration=20,
            category='Cardio',
            exercises=['Jumping jacks', 'Running'],
            recommended_for='Beginners'
        )
    
    def test_workout_creation(self):
        """Test that a workout can be created"""
        self.assertEqual(self.workout.name, 'Beginner Cardio')
        self.assertEqual(self.workout.difficulty, 'Easy')
        self.assertEqual(self.workout.category, 'Cardio')


class UserAPITest(APITestCase):
    """Test cases for User API endpoints"""
    
    def setUp(self):
        """Set up test data"""
        self.user_data = {
            'email': 'api@example.com',
            'username': 'apiuser',
            'password': 'apipass123',
            'full_name': 'API User',
            'team': 'Team Beta'
        }
        self.user = User.objects.create(**self.user_data)
    
    def test_get_users_list(self):
        """Test getting list of users"""
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_user(self):
        """Test creating a new user"""
        new_user_data = {
            'email': 'new@example.com',
            'username': 'newuser',
            'password': 'newpass123',
            'full_name': 'New User',
            'team': 'Team Gamma'
        }
        response = self.client.post('/api/users/', new_user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TeamAPITest(APITestCase):
    """Test cases for Team API endpoints"""
    
    def setUp(self):
        """Set up test data"""
        self.team_data = {
            'name': 'API Team',
            'description': 'Test team for API',
            'captain': 'apiuser',
            'members': ['user1', 'user2'],
            'total_points': 200
        }
        self.team = Team.objects.create(**self.team_data)
    
    def test_get_teams_list(self):
        """Test getting list of teams"""
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_team(self):
        """Test creating a new team"""
        new_team_data = {
            'name': 'New Team',
            'description': 'New test team',
            'captain': 'newcaptain',
            'members': [],
            'total_points': 0
        }
        response = self.client.post('/api/teams/', new_team_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ActivityAPITest(APITestCase):
    """Test cases for Activity API endpoints"""
    
    def test_get_activities_list(self):
        """Test getting list of activities"""
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_activity(self):
        """Test creating a new activity"""
        activity_data = {
            'user': 'testuser',
            'activity_type': 'Cycling',
            'duration': 45,
            'distance': 15.0,
            'calories': 400,
            'points': 75,
            'date': datetime.now().isoformat(),
            'notes': 'Evening ride'
        }
        response = self.client.post('/api/activities/', activity_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class LeaderboardAPITest(APITestCase):
    """Test cases for Leaderboard API endpoints"""
    
    def test_get_leaderboard(self):
        """Test getting leaderboard"""
        response = self.client.get('/api/leaderboard/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class WorkoutAPITest(APITestCase):
    """Test cases for Workout API endpoints"""
    
    def test_get_workouts_list(self):
        """Test getting list of workouts"""
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_workout(self):
        """Test creating a new workout"""
        workout_data = {
            'name': 'Advanced Strength',
            'description': 'For experienced users',
            'difficulty': 'Hard',
            'duration': 60,
            'category': 'Strength',
            'exercises': ['Deadlifts', 'Squats'],
            'recommended_for': 'Advanced'
        }
        response = self.client.post('/api/workouts/', workout_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
