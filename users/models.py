from contextlib import nullcontext
from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver



# Create your models here.
# One to One relationship with User and Profile
STACK_CHOICES = (
    ('frontend', 'FRONTEND'),
    ('backend', 'BACKEND'),
    ('fullstack','FULLSTACK'),
    ( 'uxdesigner', 'UXDESIGNER'),
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True) 
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True) 
    username = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    stack = models.CharField(max_length=20, choices= STACK_CHOICES, default='fullstack')
    about_me = models.CharField(max_length=200, blank=True, null=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='profiles/', default="profiles/default_profile.png")
    social_github = models.CharField(max_length=200, blank=True, null=True)
    social_linkedin = models.CharField(max_length=200, blank=True, null=True)
    social_twitter = models.CharField(max_length=200, blank=True, null=True)
    social_website = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add= True)
    id = models.UUIDField(default = uuid.uuid4, unique= True, primary_key=True,editable=False)
    # project_info = models.ManyToManyField(Project,on_delete = models.CASCADE, null=True,blank=True)

    
    def __str__(self):
        return str(self.username)
    
class Skill(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add= True)
    id = models.UUIDField(default = uuid.uuid4, unique= True, primary_key=True,editable=False)
    
    def __str__(self):
        return str(self.name)
