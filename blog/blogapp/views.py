from django.shortcuts import get_object_or_404, redirect, render
from .models import Post, Category
from .forms import CommentForm
from django .db.models import Q

def detail(request, category_slug, slug):
    post = get_object_or_404(Post, slug=slug, status=Post.ACTIVE)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            
            return redirect('post_detail', slug=slug)
    else:
        form = CommentForm()
    
        
    return render(request,'blogapp/details.html', {'post': post, 'form': form})

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(status=Post.ACTIVE)
    
    return render(request, 'blogapp/category.html', {'category': category, 'posts': posts})

def search(request):
    query = request.GET.get('query','')
    
    posts = Post.objects.filter(status=Post.ACTIVE).filter(Q(title__icontains=query) | Q(intro__icontains=query) | Q(body__icontains=query))
    
    return render(request, 'blogapp/search.html', {'posts': posts, 'query': query})