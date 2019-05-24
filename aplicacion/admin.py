from django.contrib import admin
from .models import User
from .models import Post
from .models import Comment

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'city', 'age', 'reg_date')
 
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date')   

class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'date')
    
admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)