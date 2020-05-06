from django.urls import path
from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView

from . import views

app_name = 'fitshare'
urlpatterns = [
    path('', views.index, name='index'),
    path('workouts/', views.workouts, name='workouts'),
    path('view_workout/<int:workout_id>/', views.view_workout, name='view_workout'),
    path('user/<int:user_id>/', views.user_profile, name='user'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.FitshareLogin.as_view(template_name='fitshare/login.html'), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
]
