from django.forms import ModelForm
from django import forms 
from .models import Project

# creates form based on Project model from models.py
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields =  ['title', 'featured_image', 'description', 'github','tags'] # will show all attribute from Project model
        widgets ={
            'tags': forms.CheckboxSelectMultiple(),
        }
        
