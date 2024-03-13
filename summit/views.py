from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.http import HttpResponse
import csv
# Create your views here.
# @login_required(login_url='loginf')
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def tracks(request):
    return render(request,'tracks.html')

def gallery(request):
    return render(request,'gallery.html')

def chief_patron(request):
    return render(request,'chiefpatrons.html')

def patrons_advisors(request):
    return render(request,'patronsadvisors.html')

def conveners(request):
    return render(request,'conveners.html')

def students(request):
    return render(request,'students.html')

def secretary(request):
    return render(request, 'secretary.html')

def registerf(request):
    print("in regf ")
    if request.method == 'POST':
        print("in post ")   
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print("in validation ")
            user = form.save()
            profile=Profile()	
            profile.user = user
            profile.dept = request.POST.get('department')
            profile.idno = request.POST.get('idno')
            profile.collage = request.POST.get('collage')
            profile.phno = request.POST.get('phno')
            profile.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=password)
            login(request, user)
            return redirect('home')
        else:
            print(form.errors)
            return render(request, "registrations.html", {"form": form})
    return render(request, "registrations.html")

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
            return render(request, 'login.html', {"errors":errors})
    return render(request,'login.html')

def logoutf(request):
    logout(request)
    return redirect('/')

def profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except:
        profile = Profile(user=request.user)
    
    return render(request,'profile.html', {'profile':profile}) 

def editprofile(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except:
        profile = Profile(user=request.user)
    message = ''
    if request.method == 'POST':
        profile.dept = request.POST.get('department')
        profile.idno = request.POST.get('idno')
        profile.collage = request.POST.get('collage')
        profile.phno = request.POST.get('phno')
        profile.save()
        message = 'Changes saved successfully!'
    return render(request,'editprofile.html', {'profile':profile, 'message':message})

def download_csv(request):
    if request.user.is_superuser:
        profiles = Profile.objects.all()

        # Set up CSV response
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="profiles.csv"'

        writer = csv.writer(response)
        writer.writerow(['Username', 'ID number', 'Collage', 'Phone no', 'Department'])  # Replace with your model field names

        for profile in profiles:
            writer.writerow([profile.user, profile.idno, profile.collage, profile.phno, profile.dept])

        return response
    return None