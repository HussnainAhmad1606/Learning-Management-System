from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="homepage"),
    path("courses/", views.courses, name="courses"),
    path("video/<str:name>", views.specificVideo, name="video"),
    path("about/", views.about, name="about")

]
