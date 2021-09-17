from django.contrib import admin

from .models import Blog, user_comment


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'date_created')
    list_filter = ['date_created', 'updated_on']
    search_fields = ['title', 'content']

class user_commentAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'date_created')
    list_filter = ['date_created']

admin.site.register(Blog, BlogAdmin)
admin.site.register(user_comment)
