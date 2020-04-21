from django.urls import path

from . import views

app_name = 'fitshare'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create_workout/', views.create_workout, name='create_workout'),
    path('create_workout_submit', views.create_workout_submit, name='create_workout_submit')
]
