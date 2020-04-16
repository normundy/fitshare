from django.conf import settings
from django.db import models
import datetime

class WorkoutType(models.Model):
    type = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.type

class ExerciseType(models.Model):
    type = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.type

class ExerciseTarget(models.Model):
    target = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.target

class ExerciseClassification(models.Model):
    utility = models.CharField(max_length=200, unique=True)
    mechanic = models.CharField(max_length=200, unique=True)
    force = models.CharField(max_length=200, unique=True)

class ExerciseInstruction(models.Model):
    preparation = models.TextField()
    execution = models.TextField()

class Workout(models.Model):
    name = models.CharField(max_length=200)
    type_id = models.ForeignKey(WorkoutType, on_delete=models.CASCADE)
    created_date = models.DateTimeField('created date')
    updated_date = models.DateTimeField('updated date')

    def __str__(self):
        return self.name

class Exercise(models.Model):
    name = models.CharField(max_length=200)
    type_id = models.ForeignKey(ExerciseType, on_delete=models.CASCADE)
    target_id = models.ForeignKey(ExerciseTarget, on_delete=models.CASCADE)
    classification_id = models.ForeignKey(ExerciseClassification, on_delete=models.CASCADE)
    instruction_id = models.ForeignKey(ExerciseInstruction, on_delete=models.CASCADE)
    created_date = models.DateTimeField('created date')
    updated_date = models.DateTimeField('updated date')

    def __str__(self):
        return self.name

class Workout_e(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    workout_id = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercise_id = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    desc = models.CharField(max_length=200)
    sets = models.IntegerField()
    reps = models.IntegerField()

    def __str__(self):
        return self.desc
