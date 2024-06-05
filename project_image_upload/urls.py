from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
  TokenObtainPairView,
  TokenRefreshView,
)
from app_image_upload.views import *
from django.conf import settings
from django.urls import path, include
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from rest_framework import routers
from app_image_upload.views import *

router = routers.DefaultRouter()

router.register(r'user-posts', UserPostViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', get_profile),
    path('refresh/', TokenRefreshView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('get-profile/', get_profile),
    path('create-user/', create_user),
    path('create-image/', create_image),
    path('get-images/', get_images),
    path('delete-image/', delete_image),
    path('like-image/', like_image),
    path('add-post/', add_post),
    path('get-posts/', get_posts),
    path('edit-post/', edit_post),
    path('delete-post/', delete_post),
    path('like-post/', like_post)
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)