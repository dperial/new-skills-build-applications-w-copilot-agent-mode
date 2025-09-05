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
        team_names = [f'Marvel{i}' for i in range(1, 11)] + [f'DC{i}' for i in range(1, 11)]
        teams = [Team.objects.create(name=name) for name in team_names]

        # Users
        users = []
        for i in range(1, 21):
            team = 'Marvel'+str(i) if i <= 10 else 'DC'+str(i-10)
            user = User.objects.create(
                name=f'Hero{i}',
                email=f'hero{i}@example.com',
                team=team
            )
            users.append(user)

        # Activities
        activity_types = ['Running', 'Cycling', 'Swimming', 'Yoga', 'Boxing']
        for i in range(1, 21):
            Activity.objects.create(
                user=users[i-1].name,
                type=activity_types[i % len(activity_types)],
                duration=20 + i,
                date=f'2025-09-{(i%30)+1:02d}'
            )

        # Leaderboard
        for i, team in enumerate(teams):
            Leaderboard.objects.create(
                team=team.name,
                points=50 + i*5
            )

        # Workouts
        for i in range(1, 21):
            Workout.objects.create(
                name=f'Workout{i}',
                description=f'Description for workout {i}',
                difficulty=['Easy', 'Medium', 'Hard'][i % 3]
            )

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with 20 test examples in chaque table.'))
