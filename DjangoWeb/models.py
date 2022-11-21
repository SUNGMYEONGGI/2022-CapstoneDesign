from django.db import models

class Student(models.Model):
    studentID = models.IntegerField()
    name = models.CharField(max_length=20)
    major = models.CharField(max_length=20)
