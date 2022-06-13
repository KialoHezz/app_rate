from django.forms import ModelForm
from django import forms
from .models import Projects,Rate

class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ('title', 'description','image')

class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = '__all__'