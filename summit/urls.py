from django.urls import path, include
from.views import *

urlpatterns = [
    path("", home,name="home"),
    path("register", registerf, name="registerf"),
    path("login", loginf, name="loginf"),
    path("logout", logoutf, name="logoutf"),
]