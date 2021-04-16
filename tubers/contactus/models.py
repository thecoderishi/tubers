from django.db import models

# Create your models here.

class ContactForm(models.Model):
    full_name = models.CharField(max_length=50)
    phone = models.IntegerField(blank=True)
    email = models.CharField(max_length=50)
    company = models.CharField(max_length=50, blank=True)
    subject = models.CharField(max_length=50)
    message = models.TextField()