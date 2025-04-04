from django.urls import path
from . import views

urlpatterns = [
       path('', views.landingPage),
       path('register', views.registerStudent),
       path('dashboard', views.Dashboard),
       path('form', views.form),
       path('conformation', views.conformation),
       path('course', views.course),
       path('Studentslist', views.Studentslist),
       path('studentdashboard', views.studentdashboard),
       path('result', views.result),
       path('api/register', views.register),
       path('api/login', views.login_view),

]