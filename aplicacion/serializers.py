from rest_framework import serializers
from .models import User
from .models import Post
from .models import Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'last_name', 'city', 'age', 'reg_date')
        
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'date', 'created_by')
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'text', 'date', 'user')