from django.http import HttpResponseRedirect
from django.views import generic
from django.utils import timezone
from django.shortcuts import render
from django.urls import reverse

from .models import Workout_e, Workout

class IndexView(generic.ListView):
    template_name = 'fitshare/index.html'
    context_object_name = 'new_workout_list'

    def get_queryset(self):
        return Workout_e.objects.select_related()

def create_workout(request):
    return render(request, 'fitshare/create_workout.html')

def create_workout_submit(request):
    try:
        workout_name = request.POST['workout_name']
        workout_type = request.POST['workout_type']
        workout_created_date = timezone.now()
        workout_updated_date = timezone.now()
        workout = Workout(name=workout_name, type=workout_type, \
            created_date=workout_created_date, updated_date=workout_updated_date)
        workout.save()
    except (KeyError):
        return render(request, 'fitshare/create_workout.html', {
            'notification': "Error creating workout",
        })
    return HttpResponseRedirect(reverse('fitshare:create_workout'), {
        'notification': "Workout created",
    })
