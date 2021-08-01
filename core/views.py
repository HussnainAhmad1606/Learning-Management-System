from django.http import HttpResponse

def index(request):
	return HttpResponse("Welcome to the Website Homepage")


def handleLogin(request):
	return HttpResponse("Sign In Page")


def courses(request):
	return HttpResponse("All Courses Page")

def handleSignup(request):
	return HttpResponse("Sign Up Page")


def specificCourse(request, name):
	return HttpResponse(f"{name} Course Website")


def handleLogout(request):
	return HttpResponse("You have logged out successfully")