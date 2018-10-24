from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from .models import Project, Profile
from django.contrib.auth.models import User
from .forms import SignupForm, ProjectForm, ProfileForm,ContentForm,UsabilityForm,DesignForm
from django.utils.encoding import force_bytes, force_text

# Create your views here.

@login_required(login_url='/accounts/login/')
def awards(request):
    form=DesignForm()
    projects = Project.objects.all()

    return render(request,'awards.html', {"projects": projects, "form":form})

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
    if 'project_name' in request.GET and request.GET['project_name']:
        search_term = request.GET.get('project_name')
        projects = Project.search_by_projects(search_term)
        message = f'{search_term}'

        return render(request, 'search.html',{'message':message, 'projects':projects})
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
            edit.Profile = request.user.profile
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



@login_required(login_url='/login')
def add_usability(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = UsabilityForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.project = project
            rate.user_name = request.user
            rate.profile = request.user.profile

            rate.save()
        return redirect('awards')

    return render(request, 'awards.html')

@login_required(login_url='/login')
def add_design(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = DesignForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.project = project
            rate.user_name = request.user
            rate.profile = request.user.profile

            rate.save()
        return redirect('awards')
    else:
        form = DesignForm()

    return render(request, 'awards.html',{'form': form})


@login_required(login_url='/login')
def add_content(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = ContentForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.project = project
            rate.user_name = request.user
            rate.profile = request.user.profile

            rate.save()
        return redirect('awards')

    return render(request, 'awards.html')


