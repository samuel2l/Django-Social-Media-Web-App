from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

# Create your models here.


from django.contrib.auth.models import User

class Profile(models.Model):
    user=models.OneToOneField(User,primary_key=True,related_name='profile',verbose_name='profile',on_delete=models.CASCADE)

    # related_name='profile',   # Allows you to access the profile from the User model using 'user.profile'.
    dp=models.ImageField(default='default.jpg',upload_to='dps')
    bio=models.TextField(max_length=250)
    location=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    followers=models.ManyToManyField(User,blank=True,related_name='followers')

    def __str__(self):
        return f"{self.user.username}'s Profile"

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
#     sender: The model class that sends the signal (User in this case).
# instance: The actual instance of the model that's sending the signal.
# created: A boolean indicating whether a new instance was created.
# **kwargs: Additional keyword arguments.
    if created:  
        Profile.objects.create(user=instance)
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

class Post(models.Model):
    content=models.TextField()
    date_created=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    likes=models.ManyToManyField(User,related_name='likes',blank=True)
    
class Comment(models.Model):
    content=models.TextField()
    date_created=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    likes=models.ManyToManyField(User,related_name='comment_likes',blank=True)


    





