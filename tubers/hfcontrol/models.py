from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class HFControl(models.Model):
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address = RichTextField()
    fb_link = models.CharField(max_length=50)
    insta_link = models.CharField(max_length=50)
    tweeter_link = models.CharField(max_length=50)
    youtube_link = models.CharField(max_length=50)

    def __str__(self):
        return self.email