from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    city = models.CharField(max_length=50, blank=False, null=False)
    age = models.IntegerField()
    reg_date = models.DateTimeField()
    
    def __str__(self):
        return self.name


class Post(models.Model):
    created_by = models.ForeignKey('User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=50, blank=False, null=False)
    date = models.DateTimeField()
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    date = models.DateTimeField()
    
    def __str__(self):
        return self.text
    
    