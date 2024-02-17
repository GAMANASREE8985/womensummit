from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def home(request):
    return render(request,'home.html')

def registerf(request):
    return render(request,'registrations.html')

def loginf(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'username or password is incorrect')
            errors = "Invalid username or password"
            return render(request, 'registrations.html', {"errors":errors})
    return render(request,'registrations.html')

def logoutf(request):
    logout(request)
    return redirect('/')