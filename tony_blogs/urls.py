"""Defines URL patterns for tony_blogs."""
from django.urls import path

from . import views

app_name = 'tony_blogs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all blog posts
    path('blog_list', views.blog_list, name='blogs'),
    # Detail page for single blog
    path('blog_detail<int:blog_id>', views.blog_detail, name='blog'),
    # Page for adding a new blog
    path('new_blog', views.new_blog, name='new_blog'),
    # page for delete view
    path('<int:blog_id>delete_view', views.delete_view, name='delete'),
    path('update_view<int:blog_id>', views.update_view, name='update'),
]
