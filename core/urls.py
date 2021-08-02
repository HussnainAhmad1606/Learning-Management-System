from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="homepage"),
    path("login/", views.handleLogin, name="login"),
    path("signup/", views.handleSignup, name="signup"),
    path("courses/", views.courses, name="courses"),
    path("video/<str:name>", views.specificVideo, name="video"),
    path("logout/", views.handleLogout, name="logout")
]
