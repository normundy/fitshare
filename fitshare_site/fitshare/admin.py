from django.contrib import admin
from .models import WorkoutType, ExerciseType, Workout, Exercise, Workout_e

admin.site.register(WorkoutType)
admin.site.register(ExerciseType)
admin.site.register(Workout)
admin.site.register(Exercise)
admin.site.register(Workout_e)
