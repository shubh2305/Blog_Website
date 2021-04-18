from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_posts')
    title = models.CharField(max_length=100)
    body = RichTextField(blank=True, null=True)
    date_created = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, related_name='blog_likes')

    def __str__(self):
        return str(self.title + ' -> ' + self.author.username)

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    body = RichTextField(blank=True, null=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.post)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    description = models.TextField()

    def __str__(self):
        return self.user.username + "'s Profile"

    
    