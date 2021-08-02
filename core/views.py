from django.http import HttpResponse
from django.shortcuts import render
from .models import Course, Video
def index(request):
	return render(request, "index.html")


def handleLogin(request):
	return HttpResponse("Sign In Page")


def courses(request):
	allCourses = Course.objects.all()
	params = {
	'courses': allCourses
	}
	return render(request, "courses.html", params)

def handleSignup(request):
	return HttpResponse("Sign Up Page")


def specificVideo(request, name):
	video = Video.objects.filter(video_name=name)
	print(f"Video: {video}")
	videoName = video[0].video_name.replace("-", " ")
	print(videoName)
	params = {
	"video": video[0],
	"name": videoName
	}
	return render(request, "video.html", params)


def handleLogout(request):
	return HttpResponse("You have logged out successfully")