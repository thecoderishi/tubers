from django.db import models

from ckeditor.fields import RichTextField

# Create your models here.

class Youtuber(models.Model):

    crew_choices = (
        ('solo', 'solo'),
        ('small', 'small'),
        ('large', 'large'),
    )

    camera_choices = (
        ('canon', 'canon'),
        ('nikon', 'nikon'),
        ('sony', 'sony'),
        ('fuji', 'fuji'),
        ('other', 'other'),
    )

    category_choices = (
        ('tech', 'tech'),
        ('cooking', 'cooking'),
        ('comedy', 'comedy'),
        ('vlogs', 'vlogs'),
        ('gaming', 'gaming'),
        ('code', 'code'),
    )

    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='media/ytubers/%Y/%m/')
    video_url = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    age = models.CharField(max_length=255)
    description = RichTextField()
    height = models.IntegerField()
    crew = models.CharField(choices=crew_choices, max_length=255)
    camera_type = models.CharField(choices=camera_choices,max_length=255)
    subs_count = models.CharField(max_length=255)
    category = models.CharField(choices=category_choices,max_length=255)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)


