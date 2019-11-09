from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import reverse
from django.http import HttpResponse
from django.contrib import messages
from .models import *

from .load_courses import load_courses

def home(request):
    return render(request, 'home.html')


def all_courses(request):
    courses = {
        'courses': Course.objects.all()
    }
    return render(request, 'all_courses.html', courses)

def all_directions(request):
    directions = {
        'directions': Direction.objects.order_by('code').all()
    }
    return render(request, 'all_directions.html', directions)

def course_description(request, course_id):
    course = {
        'course': Course.objects.filter(id=course_id).first()
    }
    return render(request, 'course_description.html', course)

def direction_description(request, direction_id):
    direction = {
        'direction': Direction.objects.filter(id=direction_id).first()
    }
    return render(request, 'direction_description.html', direction)

def update_courses(request):
    load_courses()
    messages.success(request, "Данные успешно обновлены!")
    return redirect(reverse(all_courses))