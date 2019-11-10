from django.apps import AppConfig
# from .models import Course, Direction
# from .load_courses import load_courses


class CoursesConfig(AppConfig):
    name = 'courses'
    
    def ready(self):
        # from .models import Course
        from .load_courses import load_courses
        # if len(Course.objects.all())==0:
        load_courses()