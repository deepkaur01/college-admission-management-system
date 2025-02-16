from django.shortcuts import render

def landingPage (request):
    return render(request,"landingPage.html")

def registerStudent(request):
    return render(request, 'registerStudent.html')

