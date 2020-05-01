from django.http import HttpResponseRedirect
from django.views import generic
from django.views import View
from django.utils import timezone
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm

from .models import Workout_e, Workout, Exercise

def index(request):
    # Get the 10 most recent workouts
    recent_workouts = Workout.objects.order_by('-updated_date')[:10]

    # Handle workout form submission
    if request.method == 'POST':
        try:
            workout_name = request.POST['workout_name']
            workout_type = request.POST['workout_type']
            workout = create_workout_tuple(workout_name, workout_type)

            exercise_name_list = []
            reps_list = []
            sets_list = []
            times_list = []
            for k, v in request.POST.items():
                if 'exercise_name' in k:
                    exercise_name_list.append(v)
                elif 'reps' in k:
                    reps_list.append(v)
                elif 'sets' in k:
                    sets_list.append(v)
                elif 'time' in k:
                    times_list.append(v)
            i = 0
            j = len(exercise_name_list)
            while (i < j):
                create_workout_e_tuple(exercise_name_list, reps_list, sets_list, times_list, i, workout, request.user)
                i = i + 1
        except (KeyError):
            return render(request, 'fitshare/index.html', {
                'notification': "Error creating workout",
            })
        return HttpResponseRedirect(reverse('fitshare:index'), {
            'notification': "Workout created",
        })

    ctx = {
        'recent_workouts': recent_workouts,
    }

    return render(request, 'fitshare/index.html', context=ctx)

def create_workout(request):
    exercises = Exercise.objects.values('name').order_by('name')
    exercises_context = {
        'exercises_context': exercises,
    }
    return render(request, 'fitshare/create_workout.html', context=exercises_context)

def view_workout(request, workout_id):
    workout_e = Workout_e.objects.filter(workout_id=workout_id).select_related()
    workout = Workout.objects.get(id=workout_id)

    # Get the 10 most recent workouts
    recent_workouts = Workout.objects.order_by('-updated_date')[:10]

    ctx = {
        'recent_workouts': recent_workouts,
        'workout_e': workout_e,
        'workout': workout,
    }

    return render(request, 'fitshare/view_workout.html', context=ctx)

def workouts(request):
    workouts = Workout.objects.all().order_by('-updated_date')

    # Get the 10 most recent workouts
    recent_workouts = Workout.objects.order_by('-updated_date')[:10]

    ctx = {
        'workouts': workouts,
        'recent_workouts': recent_workouts,
    }

    return render(request, 'fitshare/workouts.html', context=ctx)

class FitshareLogin(auth_views.LoginView):
    #template_name = 'login.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        # Get the 10 most recent workouts
        recent_workouts = Workout.objects.order_by('-updated_date')[:10]

        ctx.update({
            'recent_workouts': recent_workouts,
        })

        return ctx

def register(request):
    # Get the 10 most recent workouts
    recent_workouts = Workout.objects.order_by('-updated_date')[:10]

    ctx = {
        'recent_workouts': recent_workouts,
    }

    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
            user = User.objects.create_user(username=username, password=password)
            user.save()
        except (KeyError):
            return render(request, 'fitshare/register', {
                'notification': "Error creating user",
            })
        return HttpResponseRedirect(reverse('fitshare:index'), {
            'notification': "User created",
        })

    return render(request, 'fitshare/register.html', context=ctx)

def create_workout_tuple(workout_name, workout_type):
    workout_created_date = timezone.now()
    workout_updated_date = timezone.now()
    workout = Workout(name=workout_name, type=workout_type, \
        created_date=workout_created_date, updated_date=workout_updated_date)
    workout.save()
    return workout

def create_workout_e_tuple(exercise_name_list, reps_list, sets_list, times_list, i, workout, user):
    #user = User.objects.get(username='Guest') # Temporary guest user for testing purposes
    exercise = Exercise(name=exercise_name_list[i], created_date=timezone.now(), updated_date=timezone.now())
    exercise.save()
    workout_e = Workout_e(user=user, workout_id=workout, \
        exercise_id=exercise, sets=sets_list[i], reps=reps_list[i], time=times_list[i])
    workout_e.save()
    return workout_e
