from django.contrib import admin
from .models import Post, Comment, Profile
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ('author', 'post', 'body')


admin.site.register(Post)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Profile)