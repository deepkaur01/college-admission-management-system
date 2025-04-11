from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    name=models.CharField(max_length=255)
    category= models.CharField(max_length=255, default="Miscellaneous")
    description=models.TextField()
    duration=models.TextField()
    fees=models.FloatField()
    url=models.URLField()
    def __str__(self):
        return  f"[{self.id}] {self.name}  applicants: {len(self.applications.all())}"

class Application(models.Model):
    userid=models.ForeignKey(to=User , on_delete=models.CASCADE)
    course=models.ManyToManyField(to=Course, related_name="applications")
    def __str__(self):
        return f"[{self.id}] {self.userid.username} applied to {list(self.course.all())}"
        # for c in self.course.all() : 
        #     course += ' ' + c.name
        # return  f"{self.userid.username} {}"

class Result(models.Model):
    courseid = models.ForeignKey(Course, on_delete=models.CASCADE)
    upload = models.FileField(upload_to ='uploads/') 
    def __str__(self):
        return  f"{self.courseid.name} Result"

class LandingPageData(models.Model):
    TYPES_OF_DATA = [
        ("LN", "Latest News"),
        ("UE", "Upcoming Events"),
        ("NB", "Notice Board"),
    ]
    data = models.TextField()
    date = models.DateField(auto_now=False, auto_now_add=False)
    type_of_data = models.CharField(max_length=255, blank=True, null=True, choices=TYPES_OF_DATA)

    def __str__(self):
        return  f"{self.date} {self.data} {self.type_of_data}"
