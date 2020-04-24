from django.http import HttpResponseRedirect
from django.views import generic
from django.utils import timezone
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Workout_e, Workout, Exercise

class IndexView(generic.ListView):
    template_name = 'fitshare/index.html'
    context_object_name = 'new_workout_list'

    def get_queryset(self):
        result = {}
        w = Workout.objects.order_by('updated_date')[:10]
        for workout in w:
            result[workout] = Workout_e.objects.filter(workout_id=workout.id).select_related()
        return result

def create_workout(request):
    exercises = Exercise.objects.values('name').order_by('name')
    exercises_context = {
        'exercises_context': exercises,
    }
    return render(request, 'fitshare/create_workout.html', context=exercises_context)

def create_workout_submit(request):
    try:
        workout_name = request.POST['workout_name']
        workout_type = request.POST['workout_type']
        workout_useralias = request.POST['workout_useralias']
        workout = create_workout_tuple(workout_name, workout_type, workout_useralias)
        exercise_name_list = []
        workout_e_description_list = []
        reps_list = []
        sets_list = []
        for k, v in request.POST.items():
            if 'exercise_name' in k:
                exercise_name_list.append(v)
            elif 'workout_e_description' in k:
                workout_e_description_list.append(v)
            elif 'reps' in k:
                reps_list.append(v)
            elif 'sets' in k:
                sets_list.append(v)
        i = 0
        j = len(exercise_name_list)
        while (i < j):
            create_workout_e_tuple(exercise_name_list, workout_e_description_list, reps_list, sets_list, i, workout)
            i = i + 1
    except (KeyError):
        return render(request, 'fitshare/create_workout.html', {
            'notification': "Error creating workout",
        })
    return HttpResponseRedirect(reverse('fitshare:create_workout'), {
        'notification': "Workout created",
    })

def create_workout_tuple(workout_name, workout_type, workout_useralias):
    workout_created_date = timezone.now()
    workout_updated_date = timezone.now()
    workout = Workout(name=workout_name, type=workout_type, user_alias=workout_useralias, \
        created_date=workout_created_date, updated_date=workout_updated_date)
    workout.save()
    return workout

def create_workout_e_tuple(exercise_name_list, workout_e_description_list, reps_list, sets_list, i, workout):
    guest_user = User.objects.get(username='Guest') # Temporary guest user for testing purposes
    exercise = Exercise.objects.get(name=exercise_name_list[i])
    workout_e = Workout_e(user=guest_user, workout_id=workout, \
        exercise_id=exercise, desc=workout_e_description_list[i], \
        sets=sets_list[i], reps=reps_list[i])
    workout_e.save()
    return workout_e
