from django.shortcuts import render, redirect, get_object_or_404
from .models import Post

# Create your views here.


def blogs(request):
    post_list = Post.objects.filter(status=1).order_by('-created_on')
    return render(request, 'blogs.html', {"post_list": post_list})


def blog(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog.html', {"post": post})
