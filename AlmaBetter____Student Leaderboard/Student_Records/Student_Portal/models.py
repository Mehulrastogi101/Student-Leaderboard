from django.db import models
from django.conf import settings

class AddStudent(models.Model):
    Name = models.CharField(max_length=50)
    Rollno = models.IntegerField()
    Math = models.IntegerField()
    Physics = models.IntegerField()
    Chemistry = models.IntegerField()
    Tmarks = models.IntegerField()
    Percentage = models.FloatField()



