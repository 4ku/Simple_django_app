import re
import urllib
from urllib.request import urlopen
import json

# Сертификат нужен для get запросов - метод urlopen
import ssl

from .models import Course, Direction

def load_courses():
    ssl._create_default_https_context = ssl._create_unverified_context  
    url = "https://openedu.ru/course"
    html=urlopen(url).read().decode('UTF-8')
    print(html)
    courses_json = re.compile(r'COURSES = (.*});').findall(str(html))[0]
    groups_json = re.compile(r'GROUPS = (.*});').findall(str(html))[0]
    courses_json = json.loads(courses_json)
    groups_json = json.loads(groups_json)

    # Запись полученных данных в БД
    for group_id in groups_json.keys():
        group = groups_json[group_id]
        title = group['title']
        code = group['code']
        Direction(id = int(group_id), name = title, code = code).save()

    for course_id in courses_json.keys():
        title = courses_json[course_id]["title"]
        url = courses_json[course_id]["url"]
        course = Course(id=int(course_id), name=title, url=url)
        course.save()
        for direction_id in courses_json[course_id]["groups"]:
            direction = Direction.objects.filter(id = int(direction_id)).first()
            course.directions.add(direction)