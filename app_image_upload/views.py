from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status, viewsets

from .models import *
from .serializers import *

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_profile(request):
  user = request.user
  profile = user.profile
  serializer = ProfileSerializer(profile, many=False)
  return Response(serializer.data)

@api_view(['POST'])
@permission_classes([])
def create_user(request):
    user = User.objects.create(
        username = request.data['username'],
    )
    user.set_password(request.data['password'])
    user.save()
    profile = Profile.objects.create(
        user=user,
        first_name=request.data['first_name'],
        last_name=request.data['last_name']
    )
    profile.save()
    profile_serialized = ProfileSerializer(profile)
    return Response(profile_serialized.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def create_image(request):
  poster = Profile.objects.get(id = request.data['posted_by'])
  request.data['poster_name'] = poster.first_name
  image_serialized = ImageSerializer(data=request.data)
  if image_serialized.is_valid():
    image_serialized.save()
    return Response(image_serialized.data, status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def get_images(request):
  images = Image.objects.all()
  images_serialized = ImageSerializer(images, many=True)
  return Response(images_serialized.data)

class UserPostViewSet(viewsets.ModelViewSet):
   queryset = UserPost.objects.all()
   serializer_class = UserPostSerializer

@api_view(['DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def delete_image(request):
  image_pk = request.data['imageId']
  print(f'image pk ={image_pk}')
  image = Image.objects.get(pk=image_pk)
  image.delete()
  return Response('DELORTED')

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def like_image(request):
   user = request.data['current_user']
   profile = Profile.objects.get(pk = user)
   image_pk = request.data['image_id']
   image = Image.objects.get(pk = image_pk)
  #  request.data['title'] = image.title
  #  request.data['image'] = image.image
   if image.likes.filter(pk = image_pk).exists:
      image.likes.add(user)
      print(image.likes)
   serialized_image =ImageSerializer(image, data = request.data)
   print(serialized_image)
   if serialized_image.is_valid():
      print('valid')
      serialized_image.save()
      return Response(serialized_image.data)
   else:
      print('not valid')
      return Response(serialized_image.errors)
   
@api_view(['POST'])
@permission_classes([IsAuthenticated])
# @parser_classes([MultiPartParser, FormParser])
def add_post(request):
  # image_data = request.data['post_images']
  print(f'HUEHUEHUEHUEHUEHUEHUEHUEHUEHUEHUEHUE {request.data}')
  poster_id = request.data['posted_by']
  poster = Profile.objects.get(id=poster_id)
  poster_name = poster.first_name
  # post_image = Image.objects.get_or_create(image = image_data)
  post = UserPost.objects.create (
    title = request.data['title'],
    posted_by = poster, #update to find user with requested id
    poster_name = poster_name,
    text_content = request.data['text_content'],
    # likes = poster,
    # post_images = post_image
  )
  post.likes.set([])
  serialized_post = UserPostSerializer(post, data=request.data)
  if serialized_post.is_valid():
    serialized_post.save()
    return Response(serialized_post.data)
  return Response(serialized_post.errors)

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
@parser_classes([MultiPartParser, FormParser])
def get_posts(request):
  posts = UserPost.objects.all()
  posts_serialized = UserPostSerializer(posts, many=True)
  return Response(posts_serialized.data)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def edit_post(request):
    print(f'request = {request.data}')
    post_pk = request.data['post_pk']
    print(f'post pk ={post_pk}')
    post = UserPost.objects.get(pk=post_pk)
    request.data['posted_by'] = post.posted_by.id
    new_text = request.data['text_content']
    post.text_content = new_text
    request.data['poster_name'] = post.posted_by.first_name
    # post.likes.set(request.data['likes'])
    print(post)
    serialized_post = UserPostSerializer(post, data = request.data)
    print(serialized_post)
    # print(serialized_post.is_valid())
    if serialized_post.is_valid():
      print('valid')
      serialized_post.save()
      return Response(serialized_post.data)
    else:
      print('not valid')
      return Response(serialized_post.errors)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_post(request):
    post_pk = request.data['postId']
    print(f'post pk ={post_pk}')
    post = UserPost.objects.get(pk=post_pk)
    post.delete()
    return Response('DELORTED')

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def like_post(request):
   user = request.data['current_user']
   profile = Profile.objects.get(pk = user)
   post_pk = request.data['post_id']
   post = UserPost.objects.get(pk = post_pk)
   request.data['posted_by'] = post.posted_by.id
   request.data['text_content'] = post.text_content
   if post.likes.filter(pk = post_pk).exists:
      post.likes.add(user)
      print(post.likes)
   serialized_post = UserPostSerializer(post, data = request.data)
   print(serialized_post)
   if serialized_post.is_valid():
      print('valid')
      serialized_post.save()
      return Response(serialized_post.data)
   else:
      print('not valid')
      return Response(serialized_post.errors)