from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from django.views import View

from .models import Workout_e, Workout, Exercise
from .forms import FS_UserCreationForm

def index(request):
    template_name = 'fitshare/index.html'

    # Get the 10 most recent workouts
    recent_workouts = Workout.objects.order_by('-updated_date')[:10]

    # Handle workout form submission
    if request.method == 'POST':
        return create_workout(request)

    ctx = {
        'recent_workouts': recent_workouts,
    }

    return render(request, template_name, context=ctx)

def view_workout(request, workout_id):
    template_name = 'fitshare/view_workout.html'

    # Get the 10 most recent workouts
    recent_workouts = Workout.objects.order_by('-updated_date')[:10]

    # Get this workout
    workout = Workout.objects.get(id=workout_id)

    # Get all exercises for this workout
    workout_e = Workout_e.objects.filter(workout_id=workout_id).select_related()

    # Get the user that created this workout
    workout_user = workout_e[0].user

    ctx = {
        'recent_workouts': recent_workouts,
        'workout_e': workout_e,
        'workout': workout,
        'workout_user' : workout_user,
    }

    return render(request, template_name, context=ctx)

def workouts(request):
    template_name = 'fitshare/workouts.html'

    # Get the 10 most recent workouts
    recent_workouts = Workout.objects.order_by('-updated_date')[:10]

    # Get all workouts
    workouts = Workout.objects.all().order_by('-updated_date')

    ctx = {
        'workouts': workouts,
        'recent_workouts': recent_workouts,
    }

    return render(request, template_name, context=ctx)

class FitshareLogin(auth_views.LoginView):

    def get_context_data(self, **kwargs):
        # Get the 10 most recent workouts
        recent_workouts = Workout.objects.order_by('-updated_date')[:10]

        ctx = super().get_context_data(**kwargs)

        ctx.update({
            'recent_workouts': recent_workouts,
        })

        return ctx

def register(request):
    template_name = 'fitshare/register.html'

    # Get the 10 most recent workouts
    recent_workouts = Workout.objects.order_by('-updated_date')[:10]

    if request.method == 'POST':
        f = FS_UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Registered succesfully')
            return redirect(reverse('fitshare:index'))
    else:
        f = FS_UserCreationForm()

    ctx = {
        'recent_workouts': recent_workouts,
        'form': f,
    }

    return render(request, template_name, context=ctx)

def user_profile(request, user_id):
    template_name = 'fitshare/user.html'

    # Get the 10 most recent workouts
    recent_workouts = Workout.objects.order_by('-updated_date')[:10]

    # Get the user by id
    user = User.objects.get(id=user_id)

    # Get the workouts this user created
    workouts = Workout.objects.filter(user=user).select_related()

    # For each workout, get all exercises
    for workout in workouts:
        workout.exercises = Workout_e.objects.filter(workout_id=workout.id)

    ctx = {
        'recent_workouts': recent_workouts,
        'user': user,
        'workouts': workouts,
    }

    return render(request, template_name, context=ctx)

def create_workout_tuple(workout_name, workout_type, user):
    workout_created_date = timezone.now()
    workout_updated_date = timezone.now()

    if user.is_authenticated:
        workout = Workout(user=user, name=workout_name, type=workout_type, \
            created_date=workout_created_date, updated_date=workout_updated_date)
    else:
        anon_user = User.objects.get(username='Anonymous')
        workout = Workout(user=anon_user, name=workout_name, type=workout_type, \
            created_date=workout_created_date, updated_date=workout_updated_date)

    workout.save()

    return workout

def create_workout_e_tuple(exercise_name_list, reps_list, sets_list, times_list, i, workout, user):
    if user.is_authenticated:
        exercise = Exercise(user=user, name=exercise_name_list[i], created_date=timezone.now(), updated_date=timezone.now())
        workout_e = Workout_e(user=user, workout_id=workout, \
            exercise_id=exercise, sets=sets_list[i], reps=reps_list[i], time=times_list[i])
    else:
        anon_user = User.objects.get(username='Anonymous')
        exercise = Exercise(user=anon_user, name=exercise_name_list[i], created_date=timezone.now(), updated_date=timezone.now())
        workout_e = Workout_e(user=anon_user, workout_id=workout, \
            exercise_id=exercise, sets=sets_list[i], reps=reps_list[i], time=times_list[i])

    exercise.save()
    workout_e.save()

    return workout_e

def create_workout(request):
    template_name = 'fitshare/index.html'

    # Get the 10 most recent workouts
    recent_workouts = Workout.objects.order_by('-updated_date')[:10]

    ctx = {
        'recent_workouts': recent_workouts,
    }

    try:
        # Create Workout
        workout_name = request.POST['workout_name']
        workout_type = request.POST['workout_type']
        user = request.user
        workout = create_workout_tuple(workout_name, workout_type, user)

        # Create Workout_e
        exercise_name_list = []
        reps_list = []
        sets_list = []
        times_list = []
        for k, v in request.POST.items():
            if 'exercise_name' in k:
                exercise_name_list.append(v)
            elif 'reps' in k:
                if v == '':
                    v = 0
                reps_list.append(v)
            elif 'sets' in k:
                if v == '':
                    v = 0
                sets_list.append(v)
            elif 'time' in k:
                if v == '':
                    v = 0
                times_list.append(v)
        i = 0
        j = len(exercise_name_list)
        while (i < j):
            create_workout_e_tuple(exercise_name_list, reps_list, sets_list, times_list, i, workout, request.user)
            i = i + 1

    except (KeyError):
        ctx.update({
            'error_message': 'Error creating workout',
        })
        return render(request, template_name, context=ctx)

    ctx.update({
        'error_message': 'Workout created',
    })

    return render(request, template_name, context=ctx)
