from django.db import models

# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Ninja(models.Model):
     DOJO = 
     first_name = models.CharField(max_length=255)
     last_name = models.CharField(max_length=255)
     create_at = models.DateTimeField(auto_now_add=True)
     update_at = models.DateTimeField(auto_now=True)
