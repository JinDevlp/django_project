from email.policy import default
from tokenize import blank_re
from django.db import models
import uuid
from users.models import Profile
# Create your models here.
# 1. python3 manage.py makemigrations 
# 2. python3 manage.py migrate     
# register the models in admin.py

""" 
queryset = Variable that holds response
ModelName = Model name
.objects = Model objects attribute
.all,get,filter,exclude = Method

    queryset = ModelName.objects.all()
    queryset = ModelName.objects.get(attribute ="value") get single object
    queryset = ModelName.objects.filter(attribute ="value")
    queryset = ModelName.objects.exclude(attribute ="value")
"""

# Many to One relationship One User Many Projects
class Project(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True,on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(null=True, blank= True, default="default.jpg")
    github = models.CharField(max_length=500,null=True, blank=True)
    tags = models.ManyToManyField('Tag',blank=True)
    # members = models.ManyToManyField('ProjectMembers',blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add= True)
    id = models.UUIDField(default = uuid.uuid4, unique= True, primary_key=True,editable=False)
    
    def __str__(self):
        return self.title

class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )
    #owner =
    project_review = models.ForeignKey(Project, on_delete= models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add= True)
    id = models.UUIDField(default = uuid.uuid4, unique= True, primary_key=True,editable=False)
    
    def __str__(self):
        return self.value

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add= True)
    id = models.UUIDField(default = uuid.uuid4, unique= True, primary_key=True,editable=False)
    
    def __str__(self):
        return self.name

# class ProjectMembers(models.Model):
#     member = models.ForeignKey(Profile, null=True,on_delete= models.SET_NULL)
#     project_info = models.ForeignKey(Project, null=True,on_delete= models.SET_NULL)
#     joined = models.DateTimeField(auto_now_add= True)
#     id = models.UUIDField(default = uuid.uuid4, unique= True, primary_key=True, editable=False)
    
#     def __str__(self):
#         return self.member.username