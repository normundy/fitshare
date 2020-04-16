from django.http import HttpResponseRedirect
from django.views import generic
from django.utils import timezone

from .models import Workout

class IndexView(generic.ListView):
    template_name = 'fitshare/index.html'
    context_object_name = 'new_workout_list'

    def get_queryset(self):
        """
        Return 10 of the most recent workouts
        """
        return Workout.objects.filter(
            created_date__lte=timezone.now()
        ).order_by('-created_date')[:10]
