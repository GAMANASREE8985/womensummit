from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    idno = models.CharField(max_length=20, default='0')
    collage = models.CharField(max_length=30, default='')
    phno = models.CharField(max_length=30, default='0')
    dept = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.idno
