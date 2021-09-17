from django import forms

from .models import Blog, user_comment


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content']

class user_commentForm(forms.ModelForm):
    class Meta:
        model = user_comment
        fields = ['author', 'content']
