from django.db import models

# Create your models here.
class Course(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=220)
    url = models.CharField(max_length=220)
    directions = models.ManyToManyField('Direction')

class Direction(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=220)
    code = models.CharField(max_length=220)
    class Meta:
        ordering = ['code']