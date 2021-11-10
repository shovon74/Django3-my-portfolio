from django.shortcuts import render,get_object_or_404
from .models import Blog


def blog(request):
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blog/blog.html', {'blogs': blogs})


def blog_detail(request, blog_id):
    blog_id = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/blog_detail.html', {'blog_id': blog_id})
