from django.http import HttpResponse
from rest_framework import viewsets
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer
def home_view(request):
    """
    Vue d'accueil pour la racine du site.
    Affiche un message de bienvenue pour Octofit Tracker.
    """
    # Access the request parameter to avoid unused variable error
    user_agent = request.META.get('HTTP_USER_AGENT', 'unknown')
    return HttpResponse(f"Bienvenue sur Octofit Tracker ! L’API fonctionne. Votre navigateur: {user_agent}")
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
