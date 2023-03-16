from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from django.contrib.auth import get_user_model

from .models import Post
from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly

class PostViewSet(viewsets.ModelViewSet):
    permissiong_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

