from dataclasses import field
from xml.parsers.expat import model
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User 
        fields = [
            'first_name', 'email', 'username', 'password1', 'password2'
        ]
        labels = {
            'first_name' : 'Name',
            
        }
        
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields =['name','email','username','location','stack','about_me','profile_image','social_github','social_linkedin', 'social_twitter','social_website']