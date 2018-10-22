from django.test import TestCase
from .models import Profile,Project, DesignRating, UsabilityRating, ContentRating

# Create your tests here.
class ProfileTestClass(TestCase):
    #set up method
    def setUp(self):
        self.nicholas = Profile(bio = 'nicholas')
    #testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.nicholas,Profile))
    #testing save method
    def test_save_profile(self):
        self.nicholas.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 1)


    #testng for deleting method
    def test_delete_profile(self):
        self.nicholas.save_profile()
        self.nicholas.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 1)


class ProjectTestClass(TestCase):
    #set Up method
    def setUp(self):
        self.testproject = Project(image = 'testproject')
    #test  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.testproject,Project))
    #testing for saving method
    def test_save_project(self):
        self.testproject.save_project()
        project = Project.objects.all()
        self.assertTrue(len(project) > 0)
    #testing for deleting method
    def test_delete_project(self):
        self.testproject.save_project()
        self.testproject.delete_project()
        project = Project.objects.all()
        self.assertTrue(len(project) > 0)
    #testing for update caption
    def test_update_caption(self):
        self.testproject.save_project()
        self.testproject.update_caption()
        project = Project.objects.all()
        self.assertTrue(len(project) > 0)