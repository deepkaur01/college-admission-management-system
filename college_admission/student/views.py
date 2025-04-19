from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json
from .models import *

def landingPage (request):
    context = {
        'title': 'Landing Page',
        'data': LandingPageData.objects.all()
    }
    return render(request,"landingPage.html", context)


def registerStudent(request):
    return render(request, 'registerStudent.html')





@login_required
def Dashboard(request):
    # Check if the user is a superuser
    if request.user.is_superuser:
        return render(request, 'dashboardpage.html')
    else:
        # Redirect to a different page if the user is not a superuser
        return redirect('landingPage')  # Redirect to the landing page or any other page

def form(request):
    return render(request, 'form.html')


def conformation(request):
    return render(request, 'conformation.html')

def course(request):
    context = {
        'title': 'Course',
        'data': Course.objects.all()
    }
    return render(request, 'course.html', context)

@login_required
def Studentslist(request):
    return render(request, 'Studentslist.html')

@login_required
def studentdashboard(request):
    # Fetch applications for the logged-in user
    applications = Application.objects.filter(userid=request.user)

    # Pass the applications to the template
    return render(request, 'studentdashboard.html', {'applications': applications})

@login_required
def result(request):
    return render(request, 'result.html')

@login_required
@csrf_exempt
def apply_view(request):
    if request.method == 'POST':
        # Check if the user is authenticated
        if request.user.is_authenticated:
            # Get the course ID from the request body
            data = json.loads(request.body)
            course_id = data.get('courseId')

            try:
                # Get the course object
                course = Course.objects.get(id=course_id)

                # Create a new application
                application = Application(userid=request.user)
                application.save()  # Save the application instance first

                # Add the course to the application
                application.course.add(course)

                return JsonResponse({'success': True, 'message': 'Application submitted successfully!'})
            except Course.DoesNotExist:
                return JsonResponse({'success': False, 'message': 'Course not found.'}, status=404)
        else:
            # User is not authenticated, return a message with a redirect URL
            return JsonResponse({
                'success': False,
                'message': 'You need to register or log in to apply for a course.',
                'redirect_url': '/register'  # URL to redirect to the registration page
            }, status=403)

    return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=405)




@csrf_exempt
def register(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('register_username')
            email = data.get('register_email')
            password = data.get('register_password')
            
            print(data)

            # Create a new user
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return JsonResponse({'success': True})

        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': 'Invalid JSON.'})
        except Exception as e:
            print(e)
            return JsonResponse({'success': False, 'message': str(e)})

    return JsonResponse({'success': False, 'message': 'Invalid request method.'})

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        username = data.get('login_username')
        password = data.get('login_password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Check if the user is a superuser
            if user.is_superuser:
                return JsonResponse({'success': True, 'redirect_url': '/dashboard'})  # Redirect to admin dashboard
            else:
                return JsonResponse({'success': True, 'redirect_url': '/studentdashboard'})  # Redirect to student dashboard
        else:
            return JsonResponse({'success': False, 'message': 'Invalid credentials.'})

    return JsonResponse({'success': False, 'message': 'Invalid request method.'})

       