from django.urls import path
from . import views
from .models import Course, Direction

urlpatterns = [
    path('', views.home),
    path('home/', views.home),
    path('all_courses/', views.all_courses, name='all_courses'),
    path('all_directions/', views.all_directions, name='all_directions'),
    path('course/<int:course_id>/', views.course_description, name='course_description'),
    path('direction/<int:direction_id>/', views.direction_description, name='direction_description'),
    path('update_courses/', views.update_courses, name = 'update_courses')

]

from .load_courses import load_courses

if len(Course.objects.all())==0:
    load_courses()


