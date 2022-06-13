from django.shortcuts import render,redirect
from .models import Projects
from .forms import ProjectsForm


# Create your views here.
def home(request):
    contex = {
        "projects": Projects.objects.all()
    }
    return render(request, 'home/index.html',contex)


def about(request):
    return render(request, 'home/about.html')

def search(request):

    if 'projects' in request.GET and request.GET["projects"]:
        search_term = request.GET.get("projects")
        searched_project = Projects.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'home/search.html',{"message":message,"project": searched_project})

    else:
        message = "You haven't searched for any term"
        return render(request, 'home/search.html',{"message":message})


def add_project(request):
    if request.method == 'POST':
        form = ProjectsForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect('homepage')

    else:
        form = ProjectsForm()

    cxt = {
            'form': form,
        }


    
    
    return render(request, 'home/add_project.html',cxt)