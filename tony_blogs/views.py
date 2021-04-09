from django.shortcuts import (render, redirect)
from django.contrib.auth.decorators import login_required

from django.views import generic
from .models import Blog
from .forms import BlogForm


def index(request):
    """The homes page for Tony Blog"""
    return render(request, 'tony_blogs/index.html')


def blogs(request):
    """Show all blogs"""
    blogs = Blog.objects.order_by('date_created')
    context = {'blogs': blogs}
    return render(request, 'tony_blogs/blogs.html', context)


def blog(request, blog_id):
    """Show a single topic and its details"""
    blog = Blog.objects.get(id=blog_id)
    content = blog.content
    context = {'blog': blog}
    return render(request, 'tony_blogs/blog.html', context)


@login_required
def new_blog(request):
    """Add new blog."""
    if request.method != 'POST':
        # No data submitted create a blank form
        form = BlogForm()
    else:
        # POST data submitted; process data.
        form = BlogForm(data=request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.owner = request.user
            new_blog.save()
            return redirect('tony_blogs:blogs')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'tony_blogs/new_blog.html', context)
