from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(default='default.jpg',  upload_to="projects")
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title


    @classmethod
    def search_by_title(cls,search_term):
        project = cls.objects.filter(title__icontains=search_term)
        return project
