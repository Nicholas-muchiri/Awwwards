from django.db import models
from django.contrib.auth.models import User
import numpy as np


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
        project = cls.objects.filter(project_name__icontains=search_term)
        return project

    @classmethod
    def project(cls):
        project = cls.objects.all()
        return project
    @classmethod
    def get_profile_images(cls, profile):
        projects = Project.objects.filter(Profile__pk = profile)
        return projects

    @classmethod
    def get_single_project(cls, project_id):
        return cls.objects.get(pk=project_id)

    def average_design(self):
        all_ratings = list(map(lambda x: x.rating, self.designrating_set.all()))
        return np.mean(all_ratings)

    def average_usability(self):
        all_ratings = list(map(lambda x: x.rating, self.usabilityrating_set.all()))
        return np.mean(all_ratings)

    def average_content(self):
        all_ratings = list(map(lambda x: x.rating, self.contentrating_set.all()))
        return np.mean(all_ratings)

    def __str__(self):
        return self.title



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



class DesignRating(models.Model):
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
        (10, '10')
    )
    project = models.ForeignKey(Project)
    pub_date = models.DateTimeField(auto_now=True)
    profile = models.ForeignKey(Profile)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES, default=0)


class UsabilityRating(models.Model):
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
        (10, '10')
    )
    project = models.ForeignKey(Project)
    pub_date = models.DateTimeField(auto_now=True)
    profile = models.ForeignKey(Profile)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES, default=0)


class ContentRating(models.Model):
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
        (10, '10')
    )
    project = models.ForeignKey(Project)
    pub_date = models.DateTimeField(auto_now=True)
    profile = models.ForeignKey(Profile)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES, default=0)