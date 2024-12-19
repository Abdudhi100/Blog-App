from django.shortcuts import render, get_object_or_404 #the view file can connect the database with the templates by importing render from django.shortcuts
from .models import Post #post class has to be imported from the model to connect the model with the templates

def blog_list(request): #this uses an http request to render the template from the request received from the client
    posts = Post.objects.all().order_by('-created_at') #this orders the model to render the Post object and order them by the sequence of when they were created
    return render (request, 'blog/blog_list.html', {'posts': posts})

def blog_detail(request, id): #another view function that renders the model for a blog post when requested
    post = get_object_or_404(Post, id=id)
    return render (request, 'blog/blog_detail.html', {'post': post})
    
    
# Create your views here.
