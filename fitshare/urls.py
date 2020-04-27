from django.urls import path

from . import views

app_name = 'fitshare'
urlpatterns = [
    path('', views.index, name='index'),
    path('create_workout/', views.create_workout, name='create_workout'),
]
