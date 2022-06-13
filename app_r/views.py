from django.shortcuts import render
from .models import Projects


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
