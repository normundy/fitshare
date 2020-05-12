import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Workout, Exercise, Workout_e

def create_workout(workout_name, workout_type, exercises):
    return

class IndexViewTests(TestCase):
    def test_recent_workouts(self):
        """
        10 most recent workouts displayed on the side pane
        """
        response = self.client.get(reverse('fitshare:index'))
        self.assertEqual(response.status_code, 200)
