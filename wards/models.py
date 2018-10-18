from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    image = models.ImageField(upload_to='picture/',null=True)
    project_name = models.CharField(max_length=60)
    project_caption = models.TextField()
    Profile = models.ForeignKey(User,null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=60)

    def save_project(self):
        self.save()


    @classmethod
    def search_by_projects(cls,search_term):
        project = cls.objects.filter(profile__name__icontains=search_term)
        return project

    @classmethod
    def project(cls):
        project = cls.objects.all()
        return project
    @classmethod
    def get_profile_images(cls, profile):
        projects = Project.objects.filter(Profile__pk = profile)
        return projects



class Profile(models.Model):
    prof_pic = models.ImageField(upload_to='picture/',null=True)
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, default=1)

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

    class Meta:
        ordering = ['bio']

    @classmethod
    def search_profile(cls, name):
        profile = Profile.objects.filter(user__username__icontains=name)
        return profile

    @classmethod
    def get_by_id(cls, id):
        profile = Profile.objects.get(user=id)
        return profile

    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user=id).first()
        return profile