from django.contrib import admin

from .models import Topic, Post

admin.site.site_header = 'NR Admin'


class TopicAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name', ], }


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'posted_date',
                    'category', 'is_new', 'featured', 'archived']
    list_editable = ['is_new', 'featured', 'archived']
    list_filter = ['author', 'category', 'is_new', 'featured', 'archived']
    prepopulated_fields = {'slug': ['title', ], }


admin.site.register(Topic, TopicAdmin)
admin.site.register(Post, PostAdmin)

# Register your models here.
