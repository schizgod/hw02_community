from django.shortcuts import render, get_object_or_404
from .models import Group, Post


def index(request):
    posts = Post.objects.all()[:10]
    template = 'index.html'
    context = {
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
