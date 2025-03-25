from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField()
    duration=models.TextField()
    fees=models.FloatField()
    url=models.URLField()

class Application(models.Model):
    userid=models.ForeignKey(to=User , on_delete=models.CASCADE)
    course=models.ManyToManyField(to=Course, related_name="applications")

class Result(models.Model):
    courseid = models.ForeignKey(Course, on_delete=models.CASCADE)
    upload = models.FileField(upload_to ='uploads/') 
