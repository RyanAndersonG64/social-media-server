from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = Profile
    fields = ['id', 'first_name', 'last_name']

class ImageSerializer(serializers.ModelSerializer):
  class Meta:
    model = Image
    fields = ['title', 'created_at', 'image']

# class UserPostSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = UserPost
#     fields = ['posted_by', 'posted_at', 'text_content',]