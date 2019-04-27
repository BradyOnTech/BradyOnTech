from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models
from .models import Post, Series, Category, Topic, Explained, ResourcesTopic, ResourcesContent

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'series', 'author', 'published_date', 'status')
    list_filter = ('status', 'created', 'published_date', 'author')
    search_fields = ('title', 'content', 'series__name')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'published_date'
    ordering = ('status', 'published_date')

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

class SeriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class TopicAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class ExplainedAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'published_date', 'status')
    list_filter = ('status', 'created', 'published_date', 'author')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'published_date'
    ordering = ('status', 'published_date')

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

admin.site.register(Post,PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Series, SeriesAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Explained, ExplainedAdmin)
admin.site.register(ResourcesTopic)
admin.site.register(ResourcesContent)