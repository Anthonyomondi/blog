from django.contrib import admin

from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'date_created')
    list_filter = ['date_created']
    search_fields = ['title', 'content']


admin.site.register(Blog, BlogAdmin)
