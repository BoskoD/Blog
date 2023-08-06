from django.shortcuts import render

from blogapp.models import Post

def frontpage(request):
    posts = Post.objects.filter(status = Post.ACTIVE)
    return render(request, 'codeinflux/frontpage.html', {'posts': posts})

def about(request):
    return render(request, 'codeinflux/about.html')
