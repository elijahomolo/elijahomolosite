from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin


from .models import Post, Category

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'body',)
    prepopulated_fields = {'slug': ('title',)} # new

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)} # new

# Register your models here.
#admin.site.register(Post)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, MarkdownxModelAdmin)
