from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    age = models.IntegerField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Category(models.Model):
    title = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=255)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    short_description = models.TextField()
    description = models.TextField()
    image = models.CharField(max_length=255)
    like = models.IntegerField()
    comment = models.IntegerField()