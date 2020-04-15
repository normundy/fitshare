from django.conf import settings
from django.db import models

class WorkoutType(models.Model):
    type = models.CharField(max_length=200)

class ExerciseType(models.Model):
    type = models.CharField(max_length=200)

class Workout(models.Model):
    name = models.CharField(max_length=200)
    type_id = models.ForeignKey(WorkoutType, on_delete=models.CASCADE)

class Exercise(models.Model):
    name = models.CharField(max_length=200)
    type_id = models.ForeignKey(ExerciseType, on_delete=models.CASCADE)

class Workout_e(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    workout_id = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercise_id = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    desc = models.CharField(max_length=200)
    sets = models.IntegerField()
    reps = models.IntegerField()
