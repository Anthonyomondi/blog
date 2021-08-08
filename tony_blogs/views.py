from django.contrib.auth.decorators import login_required
from django.shortcuts import Http404, get_object_or_404, redirect, render
from django.views import generic


from .forms import BlogForm, user_commentForm
from .models import Blog


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
    blog = get_object_or_404(Blog, id=blog_id)
    context = {'blog': blog}

    comments = blog.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = user_commentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but without saving to database
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.blog = blog
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = user_commentForm()
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

# update view for details


def update_view(request, blog_id):
    # edit existing blog
    blog = Blog.objects.get(id=blog_id)
    # make sure the post belongs to the current user
    if blog.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request, pre-fill form with the current content
        form = BlogForm(instance=blog)

    else:
        # POST data submitted, process data.
        form = BlogForm(instance=blog, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('tony_blogs:blog', blog_id=blog.id)

    context = {'blog': blog, 'form': form}
    return render(request, 'tony_blogs/update_view.html', context)


@login_required
def delete_view(request, blog_id):
    # dictionary for initial data with field names as keys
    context = {}

    # fetch the object related to passed id
    blog = get_object_or_404(Blog, id=blog_id)
    # make sure the post belongs to the current user
    if blog.owner != request.user:
        raise Http404

    if request.method == "POST":
        # delete object
        blog.delete()
        # after delete redirect to homepage
        return redirect('tony_blogs:blogs')

    return render(request, 'tony_blogs/delete_view.html', context)
