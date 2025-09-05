from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Users
        ironman = User.objects.create(name='Iron Man', email='ironman@marvel.com', team='Marvel')
        captain = User.objects.create(name='Captain America', email='cap@marvel.com', team='Marvel')
        batman = User.objects.create(name='Batman', email='batman@dc.com', team='DC')
        superman = User.objects.create(name='Superman', email='superman@dc.com', team='DC')

        # Activities
        Activity.objects.create(user='Iron Man', type='Running', duration=30, date='2025-09-01')
        Activity.objects.create(user='Captain America', type='Cycling', duration=45, date='2025-09-02')
        Activity.objects.create(user='Batman', type='Swimming', duration=60, date='2025-09-03')
        Activity.objects.create(user='Superman', type='Yoga', duration=20, date='2025-09-04')

        # Leaderboard
        Leaderboard.objects.create(team='Marvel', points=75)
        Leaderboard.objects.create(team='DC', points=80)

        # Workouts
        Workout.objects.create(name='Pushups', description='Upper body strength', difficulty='Easy')
        Workout.objects.create(name='Squats', description='Lower body strength', difficulty='Medium')
        Workout.objects.create(name='Plank', description='Core strength', difficulty='Hard')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
