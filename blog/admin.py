from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post) #the admin file is used to register models
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
#this code register the Post class in the model as admin and list out some of the post class attributes
