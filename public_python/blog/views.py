from django.shortcuts import render
from .models import BlogPost


def post_detail(request, post_slug):
    post = BlogPost.objects.get(slug=post_slug)
    print(post.title)
    context = {'post': post}
    return render(request, 'blog/post_detail.html', context)
