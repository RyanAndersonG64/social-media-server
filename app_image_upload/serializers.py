from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = Profile
    fields = ['id', 'user', 'first_name', 'last_name']


class ImageSerializer(serializers.ModelSerializer):
  likes = serializers.IntegerField(source = 'likes.count', read_only = True)
  class Meta:
    model = Image
    fields = ['id', 'title','created_at', 'image', 'likes', 'posted_by', 'poster_name']

class UserPostSerializer(serializers.ModelSerializer):
  # post_images = ImageSerializer(many=True)
  likes = serializers.IntegerField(source = 'likes.count', read_only = True)
  class Meta:
    model = UserPost
    # fields = ['id', 'title', 'posted_by', 'posted_at', 'text_content', 'like_count', 'post_images']
    fields = '__all__'