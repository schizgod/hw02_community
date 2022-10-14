from django.shortcuts import render, get_object_or_404
from .models import Group, Post


split_n = 10


def index(request):
    posts = Post.objects.select_related().all()[:split_n]
    template = 'posts/index.html'
    context = {
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:split_n]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
