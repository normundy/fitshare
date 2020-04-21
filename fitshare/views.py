from django.http import HttpResponseRedirect
from django.views import generic
from django.utils import timezone

from .models import Workout_e

class IndexView(generic.ListView):
    template_name = 'fitshare/index.html'
    context_object_name = 'new_workout_list'

    def get_queryset(self):
        return Workout_e.objects.select_related()
