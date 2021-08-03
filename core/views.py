from django.http import HttpResponse
from django.shortcuts import render
from .models import Course, Video

def index(request):
	return render(request, "index.html")




def courses(request):
	allCourses = Course.objects.all()
	params = {
	'courses': allCourses
	}
	return render(request, "courses.html", params)


def specificVideo(request, name):
	video = Video.objects.filter(video_name=name)
	category = video[0].video_category
	print(category)
	allVideos = Video.objects.filter(video_category=category)
	totalVideos = len(allVideos)
	print(f"Video: {video}")
	videoName = video[0].video_name.replace("-", " ")
	print(videoName)
	params = {
	"video": video[0],
	"name": videoName,
	"allVideos": allVideos,
	"totalVideos": totalVideos
	}
	return render(request, "video.html", params)



def about(request):
	return render(request, "about.html")