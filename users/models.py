from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.TextField(max_length=120)
    name= models.TextField(blank=True , null=True)
    email = models.TextField(max_length=120)
    password= models.TextField(max_length=120)
    confirmpassword= models.TextField(max_length=120)
    types = models.TextField(max_length=1)