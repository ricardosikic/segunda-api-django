from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer
from .serializers import PostSerializer
from .serializers import CommentSerializer

from .models import User
from .models import Post
from .models import Comment

# Create your views here.
class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
class Postview(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    
 
class Commentview(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()   