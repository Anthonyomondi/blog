from django.contrib import admin

from .models import Blog, user_comment


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'date_created')
    list_filter = ['date_created', 'updated_on']
    search_fields = ['title', 'content']


admin.site.register(Blog, BlogAdmin)
admin.site.register(user_comment)
