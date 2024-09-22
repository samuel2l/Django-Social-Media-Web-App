from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


from django.contrib.auth.models import User

class Profile(models.Model):
    user=models.OneToOneField(User,primary_key=True,related_name='profile',verbose_name='profile',on_delete=models.CASCADE)

    # related_name='profile',   # Allows you to access the profile from the User model using 'user.profile'.
    dp=models.ImageField(default='default.jpg',upload_to='dps')
    bio=models.TextField(max_length=250)
    location=models.CharField(max_length=100)
    name=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username}'s Profile"

class Post(models.Model):
    content=models.TextField()
    date_created=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    
class Comment(models.Model):
    content=models.TextField()
    date_created=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)

    




