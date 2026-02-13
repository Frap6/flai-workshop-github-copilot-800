from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone
from datetime import timedelta
import random


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING('Clearing existing data...'))
        
        # Delete all existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        
        self.stdout.write(self.style.SUCCESS('Existing data cleared!'))
        
        # Create Teams
        self.stdout.write(self.style.WARNING('Creating teams...'))
        team_marvel = Team.objects.create(
            name='Team Marvel',
            description='Avengers assemble! The mightiest heroes of the Marvel Universe.',
            captain='iron_man',
            members=['iron_man', 'captain_america', 'thor', 'black_widow', 'hulk', 'spider_man'],
            total_points=0
        )
        
        team_dc = Team.objects.create(
            name='Team DC',
            description='Justice League united! Protectors of truth and justice.',
            captain='superman',
            members=['superman', 'batman', 'wonder_woman', 'flash', 'aquaman', 'green_lantern'],
            total_points=0
        )
        
        self.stdout.write(self.style.SUCCESS(f'Created {Team.objects.count()} teams'))
        
        # Create Users
        self.stdout.write(self.style.WARNING('Creating users...'))
        marvel_heroes = [
            {'username': 'iron_man', 'email': 'tony.stark@marvel.com', 'full_name': 'Tony Stark', 'password': 'jarvis123'},
            {'username': 'captain_america', 'email': 'steve.rogers@marvel.com', 'full_name': 'Steve Rogers', 'password': 'shield123'},
            {'username': 'thor', 'email': 'thor@asgard.com', 'full_name': 'Thor Odinson', 'password': 'mjolnir123'},
            {'username': 'black_widow', 'email': 'natasha.romanoff@marvel.com', 'full_name': 'Natasha Romanoff', 'password': 'widow123'},
            {'username': 'hulk', 'email': 'bruce.banner@marvel.com', 'full_name': 'Bruce Banner', 'password': 'smash123'},
            {'username': 'spider_man', 'email': 'peter.parker@marvel.com', 'full_name': 'Peter Parker', 'password': 'web123'},
        ]
        
        dc_heroes = [
            {'username': 'superman', 'email': 'clark.kent@dc.com', 'full_name': 'Clark Kent', 'password': 'krypton123'},
            {'username': 'batman', 'email': 'bruce.wayne@dc.com', 'full_name': 'Bruce Wayne', 'password': 'gotham123'},
            {'username': 'wonder_woman', 'email': 'diana.prince@dc.com', 'full_name': 'Diana Prince', 'password': 'themyscira123'},
            {'username': 'flash', 'email': 'barry.allen@dc.com', 'full_name': 'Barry Allen', 'password': 'speed123'},
            {'username': 'aquaman', 'email': 'arthur.curry@dc.com', 'full_name': 'Arthur Curry', 'password': 'atlantis123'},
            {'username': 'green_lantern', 'email': 'hal.jordan@dc.com', 'full_name': 'Hal Jordan', 'password': 'willpower123'},
        ]
        
        users_created = []
        for hero_data in marvel_heroes:
            user = User.objects.create(
                username=hero_data['username'],
                email=hero_data['email'],
                full_name=hero_data['full_name'],
                password=hero_data['password'],
                team='Team Marvel'
            )
            users_created.append(user)
        
        for hero_data in dc_heroes:
            user = User.objects.create(
                username=hero_data['username'],
                email=hero_data['email'],
                full_name=hero_data['full_name'],
                password=hero_data['password'],
                team='Team DC'
            )
            users_created.append(user)
        
        self.stdout.write(self.style.SUCCESS(f'Created {User.objects.count()} users'))
        
        # Create Activities
        self.stdout.write(self.style.WARNING('Creating activities...'))
        activity_types = ['Running', 'Cycling', 'Swimming', 'Weight Training', 'Yoga', 'Boxing', 'Hiking']
        
        for user in users_created:
            # Create 3-7 random activities per user
            num_activities = random.randint(3, 7)
            user_total_points = 0
            
            for i in range(num_activities):
                activity_type = random.choice(activity_types)
                duration = random.randint(20, 120)
                distance = round(random.uniform(2.0, 25.0), 2) if activity_type in ['Running', 'Cycling', 'Swimming', 'Hiking'] else 0.0
                calories = duration * random.randint(5, 12)
                points = duration + int(distance * 10)
                
                activity_date = timezone.now() - timedelta(days=random.randint(0, 30))
                
                Activity.objects.create(
                    user=user.username,
                    activity_type=activity_type,
                    duration=duration,
                    distance=distance,
                    calories=calories,
                    points=points,
                    date=activity_date,
                    notes=f'{activity_type} session by {user.full_name}'
                )
                
                user_total_points += points
            
            # Update team points
            if user.team == 'Team Marvel':
                team_marvel.total_points += user_total_points
            else:
                team_dc.total_points += user_total_points
        
        team_marvel.save()
        team_dc.save()
        
        self.stdout.write(self.style.SUCCESS(f'Created {Activity.objects.count()} activities'))
        
        # Create Leaderboard
        self.stdout.write(self.style.WARNING('Creating leaderboard entries...'))
        for user in users_created:
            user_activities = Activity.objects.filter(user=user.username)
            total_points = sum(activity.points for activity in user_activities)
            total_activities = user_activities.count()
            
            Leaderboard.objects.create(
                user=user.username,
                team=user.team,
                total_points=total_points,
                total_activities=total_activities,
                rank=0  # Will be calculated after all entries are created
            )
        
        # Update ranks
        leaderboard_entries = Leaderboard.objects.all().order_by('-total_points')
        for rank, entry in enumerate(leaderboard_entries, start=1):
            entry.rank = rank
            entry.save()
        
        self.stdout.write(self.style.SUCCESS(f'Created {Leaderboard.objects.count()} leaderboard entries'))
        
        # Create Workouts
        self.stdout.write(self.style.WARNING('Creating workout suggestions...'))
        workouts_data = [
            {
                'name': 'Thor\'s Hammer Strength',
                'description': 'Build god-like strength with this intense full-body workout.',
                'difficulty': 'Advanced',
                'duration': 60,
                'category': 'Strength',
                'exercises': ['Deadlifts', 'Squats', 'Bench Press', 'Pull-ups', 'Hammer Curls'],
                'recommended_for': 'Team Marvel'
            },
            {
                'name': 'Flash\'s Speed Circuit',
                'description': 'Increase speed and agility with high-intensity interval training.',
                'difficulty': 'Advanced',
                'duration': 45,
                'category': 'Cardio',
                'exercises': ['Sprint Intervals', 'Box Jumps', 'Burpees', 'High Knees', 'Mountain Climbers'],
                'recommended_for': 'Team DC'
            },
            {
                'name': 'Captain America\'s Endurance Run',
                'description': 'Build superhero endurance with this steady-state cardio workout.',
                'difficulty': 'Intermediate',
                'duration': 45,
                'category': 'Cardio',
                'exercises': ['Long Distance Run', 'Jump Rope', 'Rowing', 'Cycling'],
                'recommended_for': 'Team Marvel'
            },
            {
                'name': 'Wonder Woman\'s Warrior Training',
                'description': 'Combat-ready functional fitness for warriors.',
                'difficulty': 'Advanced',
                'duration': 50,
                'category': 'Mixed',
                'exercises': ['Battle Ropes', 'Kettlebell Swings', 'Medicine Ball Slams', 'Box Jumps', 'Push-ups'],
                'recommended_for': 'Team DC'
            },
            {
                'name': 'Spider-Man\'s Flexibility Flow',
                'description': 'Improve flexibility and balance like your friendly neighborhood Spider-Man.',
                'difficulty': 'Beginner',
                'duration': 30,
                'category': 'Flexibility',
                'exercises': ['Yoga Flow', 'Dynamic Stretching', 'Balance Poses', 'Core Work'],
                'recommended_for': 'Team Marvel'
            },
            {
                'name': 'Batman\'s Tactical Training',
                'description': 'Prepare for anything with this versatile tactical workout.',
                'difficulty': 'Advanced',
                'duration': 60,
                'category': 'Mixed',
                'exercises': ['Parkour Drills', 'Combat Training', 'Grip Strength', 'Agility Ladder', 'Core Circuit'],
                'recommended_for': 'Team DC'
            },
            {
                'name': 'Hulk\'s Power Smash',
                'description': 'Pure strength and power development.',
                'difficulty': 'Advanced',
                'duration': 55,
                'category': 'Strength',
                'exercises': ['Heavy Squats', 'Power Cleans', 'Tire Flips', 'Sled Push', 'Farmer\'s Walk'],
                'recommended_for': 'Team Marvel'
            },
            {
                'name': 'Aquaman\'s Ocean Swim',
                'description': 'Master the water with this swimming-focused workout.',
                'difficulty': 'Intermediate',
                'duration': 40,
                'category': 'Cardio',
                'exercises': ['Freestyle Swimming', 'Backstroke', 'Butterfly', 'Water Treading', 'Pool Resistance'],
                'recommended_for': 'Team DC'
            },
        ]
        
        for workout_data in workouts_data:
            Workout.objects.create(**workout_data)
        
        self.stdout.write(self.style.SUCCESS(f'Created {Workout.objects.count()} workouts'))
        
        # Summary
        self.stdout.write(self.style.SUCCESS('\n' + '='*50))
        self.stdout.write(self.style.SUCCESS('DATABASE POPULATION COMPLETE!'))
        self.stdout.write(self.style.SUCCESS('='*50))
        self.stdout.write(f'Teams: {Team.objects.count()}')
        self.stdout.write(f'Users: {User.objects.count()}')
        self.stdout.write(f'Activities: {Activity.objects.count()}')
        self.stdout.write(f'Leaderboard Entries: {Leaderboard.objects.count()}')
        self.stdout.write(f'Workouts: {Workout.objects.count()}')
        self.stdout.write(self.style.SUCCESS('='*50))
