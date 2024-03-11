from django.urls import path, include
from.views import *

urlpatterns = [
    path("", home,name="home"),
    path("about", about,name="home"),
    path("tracks", tracks,name="home"),
    path("gallery", gallery,name="home"),
    path("register", registerf, name="registerf"),
    path("login", loginf, name="loginf"),
    path("profile", profile, name="profile"),
    path("profile/edit", editprofile, name="editprofile"),
    path("logout", logoutf, name="logoutf"),
]