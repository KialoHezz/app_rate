from django.db import models
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(default='default.jpg',  upload_to="projects")

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255, blank=True)
    posted_projects = models.ForeignKey(Projects, on_delete=models.CASCADE)
    contact = models.IntegerField()
    image = models.ImageField(default='default.jpg',  upload_to="profile")

    def __str__(self):
        return f'{self.user.username} Profile'