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