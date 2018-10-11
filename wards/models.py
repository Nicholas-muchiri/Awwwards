from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='picture/',null=True)
    image_name = models.CharField(max_length=60)
    image_caption = models.TextField()
    Profile = models.ForeignKey(User,null=True)
    likes = models.BooleanField(default=False)
    pub_date = models.DateTimeField(auto_now_add=True)



    def save_image(self):
        self.save()


    @classmethod
    def search_by_profile(cls,search_term):
        picture = cls.objects.filter(profile__name__icontains=search_term)
        return picture

    @classmethod
    def pics(cls):
        image = cls.objects.all()
        return image
    @classmethod
    def get_profile_images(cls, profile):
        images = Image.objects.filter(Profile__pk = profile)
        return images
