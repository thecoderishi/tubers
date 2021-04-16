from django.db import models

# Create your models here.

class Hiretuber(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.IntegerField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    message = models.TextField(blank=True)
    tuber_id = models.IntegerField()
    tuber_name = models.CharField(max_length=50)
    tuber_city = models.CharField(max_length=50, blank=True)
    user_id = models.IntegerField(blank=True)
    tuber_price = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.email