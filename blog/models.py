from django.db import models
from django.contrib.auth.models import User,AbstractUser
# Create your models here.

class Author(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField()
    account_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='static/images', height_field=None, width_field=None, max_length=None)
    total_comment = models.IntegerField()
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    post_category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title
    