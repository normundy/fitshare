from django.conf import settings
from django.db import models
import datetime

class Workout(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200, null=True)
    created_date = models.DateTimeField('created date')
    updated_date = models.DateTimeField('updated date')

    class Meta:
        db_table = 'workout'

        constraints = [
            models.UniqueConstraint(fields=['name'], name='unique_workout_name')
        ]

    def __str__(self):
        return ("Name: " + self.name + " | Type: " + self.type)

class Exercise(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField('created date')
    updated_date = models.DateTimeField('updated date')

    class Meta:
        db_table = 'exercise'

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

    class Meta:
        db_table = 'workout_e'

    def __str__(self):
        return "Username: " + self.user.username + " | Workout: " + self.workout_id.name + " | Exercise: " + self.exercise_id.name
