from django.urls import path
from.import views

urlpatterns = [
       path('', views.landingPage),
       path('register', views.registerStudent)
]