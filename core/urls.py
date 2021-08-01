from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="homepage"),
    path("login/", views.handleLogin, name="login"),
    path("signup/", views.handleSignup, name="signup"),
    path("courses/", views.courses, name="courses"),
    path("course/<str:name>", views.specificCourse, name="course"),
    path("logout/", views.handleLogout, name="logout")
]
