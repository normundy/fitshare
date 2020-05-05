from django.conf import settings
from django.db import models
import datetime

class Workout(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200, null=True)
    created_date = models.DateTimeField('created date')
    updated_date = models.DateTimeField('updated date')

    def __str__(self):
        return ("Name: " + self.name + " | Type: " + self.type)

class Exercise(models.Model):
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200, null=True)
    target = models.CharField(max_length=200, null=True)
    utility = models.CharField(max_length=200, null=True)
    mechanic = models.CharField(max_length=200, null=True)
    force = models.CharField(max_length=200, null=True)
    preparation = models.TextField(null=True)
    execution = models.TextField(null=True)
    created_date = models.DateTimeField('created date')
    updated_date = models.DateTimeField('updated date')

    def __str__(self):
        return "Name: " + self.name

class Workout_e(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    workout_id = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercise_id = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    desc = models.CharField(max_length=200, null=True)
    sets = models.IntegerField(null = True)
    reps = models.IntegerField(null = True)
    time = models.CharField(max_length=200, null=True)

    def __str__(self):
        return "Username: " + self.user.username + " | Workout: " + self.workout_id.name + " | Exercise: " + self.exercise_id.name
