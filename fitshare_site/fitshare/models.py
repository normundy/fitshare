from django.conf import settings
from django.db import models

class WorkoutType(models.Model):
    type = models.CharField(max_length=200)

    def __str__(self):
        return self.type

class ExerciseType(models.Model):
    type = models.CharField(max_length=200)

    def __str__(self):
        return self.type

class Workout(models.Model):
    name = models.CharField(max_length=200)
    type_id = models.ForeignKey(WorkoutType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Exercise(models.Model):
    name = models.CharField(max_length=200)
    type_id = models.ForeignKey(ExerciseType, on_delete=models.CASCADE)

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
