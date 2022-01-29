from django.contrib import admin
from .models import Post, Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'nickname', 'comment')    

admin.site.register(Post)
admin.site.register(Comment, CommentAdmin)
