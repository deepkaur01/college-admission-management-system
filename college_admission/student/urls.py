from django.urls import path
from . import views

urlpatterns = [
    path('', views.landingPage, name="landingPage"),
    path('register', views.registerStudent, name="registerStudent"),
     path('accounts/login/', views.registerStudent, name="login"),
    path('dashboard', views.Dashboard, name="dashboard"),
    path('form', views.form, name="form"),
    path('conformation', views.conformation, name="conformation"),
    path('course/', views.course, name="course"),
    path('studentslist', views.Studentslist, name="studentsList"),
    path('studentdashboard', views.studentdashboard, name="studentDashboard"),
    path('result', views.result, name="result"),
    path('api/register', views.register, name="apiRegister"),
    path('api/login', views.login_view, name="apiLogin"),
    path('api/apply', views.apply_view, name="apiApply"),
]