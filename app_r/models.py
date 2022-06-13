from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
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



class Rate(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
        
    )
    
    username = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)
    rating = models.IntegerField(choices=RATING_CHOICES)