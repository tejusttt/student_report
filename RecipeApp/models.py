from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    user = models.ForeignKey( User , on_delete=models.CASCADE, blank= True , null= True )
    recipe_name = models.CharField(max_length =25, default='No name provided')
    recipe_desc= models.TextField(default='No description provided')
    recipe_image = models.ImageField(upload_to="recipe")
         