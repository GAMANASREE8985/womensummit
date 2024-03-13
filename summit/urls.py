from django.urls import path, include
from.views import *

urlpatterns = [
    path("", home,name="home"),
    path("about", about,name="home"),
    path("tracks", tracks,name="home"),
    path("gallery", gallery,name="home"),
    path("chief_patron", chief_patron,name="home"),
    path("patrons_advisors", patrons_advisors,name="home"),
    path("conveners", conveners,name="home"),
    path("secretary", secretary,name="home"),
    path("register", registerf, name="registerf"),
    path("login", loginf, name="loginf"),
    path("profile", profile, name="profile"),
    path("download/profile", download_csv, name="downloadcsv"),
    path("profile/edit", editprofile, name="editprofile"),
    path("logout", logoutf, name="logoutf"),
]