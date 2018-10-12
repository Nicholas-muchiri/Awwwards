from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from .models import Project, Profile
from django.contrib.auth.models import User
from .forms import SignupForm, ProjectForm, ProfileForm
from django.utils.encoding import force_bytes, force_text

# Create your views here.

@login_required(login_url='/login/')
def awards(request):
    # post = Image.objects.all()
    return render(request,'awards.html')

def pics(request):
    pictures = Image.objects.all()

    return render(request,'awards.html', {"pictures": pictures})

def profile(request, username):
    profile = User.objects.get(username=username)
    # print(profile.id)
    try:
        profile_details = Profile.get_by_id(profile.id)
    except:
        profile_details = Profile.filter_by_id(profile.id)
    projects = Project.get_profile_images(profile.id)
    title = f'@{profile.username} Awwwards Projects'

    return render(request, 'profile/profile.html', {'title':title, 'profile':profile, 'profile_details':profile_details, 'projects':projects})

def search(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search')
        profiles = Profile.search_profile(search_term)
        message = f'{search_term}'

        return render(request, 'search.html',{'message':message, 'profiles':profiles})
    else:
        message = 'Enter term to search'
        return render(request, 'search.html', {'message':message})


def signup(request):
    if request.user.is_authenticated():
        return redirect('signup')
    else:
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = False
                user.save()
            return redirect('awards')
        else:
            form = SignupForm()
            return render(request, 'registration/signup.html',{'form':form})


def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.user = request.user
            edit.save()
            return redirect('edit_profile')
    else:
        form = ProfileForm()

    return render(request, 'profile/edit_profile.html', {'form': form})


@login_required(login_url='/login')
def upload_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.Profile = request.user
            upload.save()
        return redirect('profile', username=request.user)
    else:
        form = ProjectForm()

    return render(request, 'profile/upload_project.html', {'form': form})


