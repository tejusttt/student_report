from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=25),
    age = models.IntegerField(),
    email = models.EmailField(max_length=254,default='example@example.com'),
    address = models.TextField() ,
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None) ,
    file = models.FileField(upload_to=None, max_length=100) ,
    flo = models.FloatField( null = True )
    
class product(models.Model):
    name = models.CharField(max_length=25),
    age = models.IntegerField(),
    email = models.EmailField(max_length=254,default='example@example.com')