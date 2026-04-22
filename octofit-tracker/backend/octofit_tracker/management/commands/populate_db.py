from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    user = models.CharField(max_length=100)
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    user = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    class Meta:
        app_label = 'octofit_tracker'

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        # Borrar datos existentes
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Crear equipos
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Crear usuarios
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='1234'),
            User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='1234'),
            User.objects.create_user(username='batman', email='batman@dc.com', password='1234'),
            User.objects.create_user(username='superman', email='superman@dc.com', password='1234'),
        ]

        # Crear actividades
        Activity.objects.create(user='ironman', activity_type='run', duration=30)
        Activity.objects.create(user='spiderman', activity_type='cycle', duration=45)
        Activity.objects.create(user='batman', activity_type='swim', duration=60)
        Activity.objects.create(user='superman', activity_type='run', duration=50)

        # Crear leaderboard
        Leaderboard.objects.create(user='ironman', points=100)
        Leaderboard.objects.create(user='spiderman', points=90)
        Leaderboard.objects.create(user='batman', points=95)
        Leaderboard.objects.create(user='superman', points=110)

        # Crear workouts
        Workout.objects.create(name='Cardio Blast', description='Intenso cardio de 30 minutos')
        Workout.objects.create(name='Fuerza Total', description='Rutina de fuerza de cuerpo completo')

        self.stdout.write(self.style.SUCCESS('La base de datos octofit_db ha sido poblada con datos de prueba.'))
