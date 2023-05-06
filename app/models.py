from django.db import models


class Human(models.Model):
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=15)
    age = models.IntegerField()


class Teacher(Human):
    experience = models.IntegerField()
