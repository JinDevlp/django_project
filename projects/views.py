from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def projects(request):
    projects = Project.objects.all()
    context = {'projects' : projects }
    return render(request, 'projects/projects.html', context)

def project_view(request,pk):
    projectObj = Project.objects.get(id=pk)
    context = {'projectObj': projectObj}
    return render(request, 'projects/single_project.html', context) # this has to be redered in html template

@login_required(login_url='login')
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('projects') #from urls.py
        
    context = {'form':form}
    return render(request, "projects/project_form.html",context)

@login_required(login_url='login')
def joinProject(request,pk):
    profile = request.user.profile
    project = Project.objects.get(id=pk)
 
    
    if request.method == 'POST':
        profile.save()
        project.save()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'projects/join_template.html', context)


@login_required(login_url='login')
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES, instance=project) # request.FILES for uploaded files 
        if form.is_valid():
            form.save()
            return redirect('projects') #from urls.py
    context = {'form':form}
    return render(request, "projects/project_form.html",context)

@login_required(login_url='login')
def deleteProject(request,pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'projects/delete_template.html', context)