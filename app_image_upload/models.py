from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
  first_name = models.TextField()
  last_name = models.TextField()

  def __str__(self):
    return self.first_name
  
class Image(models.Model):
  title = models.TextField(default = 'Pointless Default Title Because Django is Being Stupid')
  # posted_by = models.ForeignKey(Profile, on_delete = models.SET('Deleted User'))
  created_at = models.DateTimeField(auto_now_add=True)
  image = models.ImageField(upload_to='images/')
  likes = models.ManyToManyField(Profile, related_name = 'image_liked_by')

  def __str__(self):
    return self.title
  
class UserPost(models.Model):
  title = models.TextField(default = 'Untitled Post')
  posted_by = models.ForeignKey(Profile, on_delete = models.SET('Deleted User'))
  posted_at = models.DateTimeField(auto_now_add=True)
  text_content = models.TextField()
  likes = models.ManyToManyField(Profile, related_name = 'post_liked_by')
  # post_images = models.ImageField(upload_to='images', height_field=None, width_field=None, max_length=100, blank=True)