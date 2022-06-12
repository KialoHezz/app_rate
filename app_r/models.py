from django.db import models

# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(default='default.jpg',  upload_to="projects")
